using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProiectFutures
{

    enum Day
    {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
    }

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

    class Timetable
    {
        public int maxPerDay { get; set; }

        public ConcurrentDictionary<Day, ConcurrentDictionary<int, List<Class>>> Table { get; }

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
        public Timetable(int maxPerDay): this()
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
            Console.WriteLine(t);
            if (hour > 20)
            {
                day = nextDay(day);
                hour = 8;
            }

            if (day == Day.SATURDAY)
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

                if (!check(res))
                    res = await search_aux(tableClone, classesClone, day, hour + 2);
                return res;
            }
            return null;
        }

        static async Task<Timetable> search()
        {
            var classes = System.IO.File.ReadAllLines("input.txt").OfType<string>().Select(line =>
            {
                var l = line.Trim().Split(';');
                return new Class(l[1], l[0]);
            }).ToList();

            var l = new List<Task<Timetable>>();

            var watch = System.Diagnostics.Stopwatch.StartNew();

            foreach (Class c in classes)
            {
                Timetable t = new Timetable();
                t.Table[Day.MONDAY][8].Add(c);

                var clone = copy(classes);
                clone.Remove(c);

                l.Add(search_aux(t, clone, Day.MONDAY, 8));
            }
            List<Timetable> res = (await Task.WhenAll(l.ToArray())).ToList();
            watch.Stop();
            var elapsed = watch.ElapsedMilliseconds;
            Console.WriteLine($"Elapsed time: {elapsed} ms");

            return res.FirstOrDefault(r => r != null);
        }
        static void Main(string[] args)
        {
            Console.WriteLine(search().Result);
        }
    }
}
