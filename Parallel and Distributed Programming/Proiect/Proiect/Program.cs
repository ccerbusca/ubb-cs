using MPI;
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Proiect
{
    enum Day
    {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
    }

    [Serializable]
    class Class
    {
        public string Group { get; }
        public string Subject { get; }

        public Class(string Group, string Subject)
        {
            this.Group = Group;
            this.Subject = Subject;
        }

        public override bool Equals(Object obj)
        {
            //Check for null and compare run-time types.
            if ((obj == null) || !this.GetType().Equals(obj.GetType()))
            {
                return false;
            }
            else
            {
                Class p = (Class)obj;
                return Group == p.Group && Subject == p.Subject;
            }
        }

        public override string ToString()
        {
            return $"{Group} : {Subject}";
        }
    }


    [Serializable]
    class Pair<A, B>
    {
        public A left { get; set; }

        public B right { get; set; }
    }

    [Serializable]
    class Response
    {
        public List<Pair<Day, List<Pair<int, List<Class>>>>> Table { get; set; }
    }


    [Serializable]
    class Timetable
    {
        public int maxPerDay { get; set; }

        public ConcurrentDictionary<Day, ConcurrentDictionary<int, List<Class>>> Table { get; }

        public Timetable(List<Pair<Day, List<Pair<int, List<Class>>>>> table)
        {
            Table = new ConcurrentDictionary<Day, ConcurrentDictionary<int, List<Class>>>();
            if (table.Count > 0)
            {
                foreach (var e in table)
                {
                    Table[e.left] = new ConcurrentDictionary<int, List<Class>>();
                    foreach (var k in e.right)
                    {
                        Table[e.left][k.left] = k.right;
                    }
                }
            }
        }

        public List<Pair<Day, List<Pair<int, List<Class>>>>> toList()
        {
            var tl = new List<Pair<Day, List<Pair<int, List<Class>>>>>();

            foreach (Day day in (Day[])Enum.GetValues(typeof(Day)))
            {
                if (day != Day.SATURDAY)
                {
                    var bl = new List<Pair<int, List<Class>>>();
                    for (int hour = 8; hour <= 20; hour += 2)
                    {
                        bl.Add(new Pair<int, List<Class>> { left = hour, right = Table[day][hour] }) ;
                    }
                    tl.Add(new Pair<Day, List<Pair<int, List<Class>>>> { left = day, right = bl});
                }
            }

            return tl;
        }

        public Timetable()
        {
            Table = new ConcurrentDictionary<Day, ConcurrentDictionary<int, List<Class>>>();
            foreach (Day day in (Day[])Enum.GetValues(typeof(Day)))
            {
                if (day != Day.SATURDAY)
                {
                    Table[day] = new ConcurrentDictionary<int, List<Class>>();
                    for (int hour = 8; hour <= 20; hour += 2)
                    {
                        Table[day][hour] = new List<Class>();
                    }
                }
            }
        }
        public Timetable(int maxPerDay) : this()
        {
            this.maxPerDay = maxPerDay;
        }

        public override string ToString()
        {
            string s = "";

            foreach (Day day in (Day[])Enum.GetValues(typeof(Day)))
            {
                if (day != Day.SATURDAY)
                {
                    s += $"{day.ToString()}:\r\n";
                    for (int hour = 8; hour <= 20; hour += 2)
                    {
                        s += $"\t{hour.ToString().PadLeft(2, '0')}.00 :\r\n";
                        foreach (Class c in Table[day][hour])
                        {
                            s += $"\t\t{c}\r\n";
                        }
                        s += "\r\n";
                    }
                }
            }

            return s;
        }

    }
    [Serializable]
    class Payload
    {
        public List<Pair<Day, List<Pair<int, List<Class>>>>> timetable { get; set; }
        public List<Class> classes { get; set; }
        public Day day { get; set; }
        public int hour { get; set; }
    }





    class Program
    {

        static bool check(Timetable timetable)
        {
            return timetable != null && timetable.Table.ToList().All(
                pair => pair.Value.ToList().All(p => p.Value.Count == new HashSet<string>(p.Value.Select(c => c.Group)).Count &&
                               p.Value.Count == new HashSet<string>(p.Value.Select(c => c.Subject)).Count));
        }

        static Timetable copy(Timetable timetable)
        {
            Timetable newTable = new Timetable();

            foreach (Day day in (Day[])Enum.GetValues(typeof(Day)))
            {
                if (day != Day.SATURDAY)
                {
                    timetable.Table[day].ToList().ForEach(pair => pair.Value.ForEach(c => newTable.Table[day][pair.Key].Add(new Class(c.Group, c.Subject))));
                }
            }

            return newTable;
        }

        static List<Class> copy(List<Class> c)
        {
            List<Class> classes = new List<Class>();
            classes.AddRange(c);
            return classes;
        }

        static Day nextDay(Day d)
        {
            return (Day)((int)d + 1);
        }

        static async Task<Timetable> search_aux(Timetable t, List<Class> classes, Day day, int hour)
        {
            if (hour > 20)
            {
                day = nextDay(day);
                hour = 8;
            }

            if (day == Day.SATURDAY || classes.Count == 0)
            {
                return check(t) ? t : null;
            }

            foreach (Class c in classes)
            {
                var classesClone = copy(classes);
                classesClone.Remove(c);
                var tableClone = copy(t);
                tableClone.Table[day][hour].Add(c);

                var res = await search_aux(tableClone, classesClone, day, hour);
                if (!check(res) || classes.Count != 0)
                    res = await search_aux(tableClone, classesClone, day, hour + 2);
                return res;
            }
            return null;
        }


        static List<Timetable> generateTimetable(Intracommunicator comm)
        {
            RequestList requestList = new RequestList();
            List<ReceiveRequest> reqs = new List<ReceiveRequest>();

            var classes = System.IO.File.ReadAllLines("input.txt").OfType<string>().Select(line =>
            {
                var l = line.Trim().Split(';');
                return new Class(l[1], l[0]);
            }).ToList();


            int id = 1;


            foreach (Class c in classes)
            {
                if (id == comm.Size)
                    id = 1;

                Timetable t = new Timetable();
                t.Table[Day.MONDAY][8].Add(c);

                var clone = copy(classes);
                clone.Remove(c);

                comm.Send(false, id, 1);
                comm.Send(new Payload { timetable = t.toList(), classes = clone, day = Day.MONDAY, hour = 8 }, id, 0);
                reqs.Add(comm.ImmediateReceive<List<Pair<Day, List<Pair<int, List<Class>>>>>>(id++, 0));
                requestList.Add(reqs.Last());
            }

            requestList.WaitAll();

            for (int i = 1; i < comm.Size; i++)
            {
                comm.Send(true, i, 1);
            }

            return reqs.Select(r =>
            {
                r.Wait();
                return new Timetable((List<Pair<Day, List<Pair<int, List<Class>>>>>)r.GetValue());
            }).Where(t => t.Table.Count != 0).ToList();
        }

        static void Main(string[] args)
        {
            MPI.Environment.Run(ref args, comm =>
            {
                if (comm.Rank == 0)
                {
                    var watch = System.Diagnostics.Stopwatch.StartNew();

                    var res = generateTimetable(comm);

                    watch.Stop();
                    var elapsed = watch.ElapsedMilliseconds;
                    Console.WriteLine($"Parallel Elapsed time: {elapsed} ms");
                    Console.WriteLine("123");
                    Console.WriteLine(String.Join('\n', res));
                }
                else
                {
                    bool finished = false;
                    while (!finished)
                    {
                        finished = comm.Receive<bool>(0, 1);
                        if (!finished)
                        {
                            var r = comm.Receive<Payload>(0, 0);
                            search_aux(new Timetable(r.timetable), r.classes, r.day, r.hour).ContinueWith(task =>
                            {
                                var l = task.Result;
                                comm.Send(l != null ? l.toList() : new List<Pair<Day, List<Pair<int, List<Class>>>>>(), 0, 0);
                            });
                        }
                    }
                }
            });
        }
    }
}
