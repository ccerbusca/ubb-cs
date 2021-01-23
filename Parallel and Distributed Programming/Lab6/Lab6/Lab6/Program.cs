using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Linq;

namespace Lab6
{

    class Graph
    {
        public int vertices { get; set; }
        ConcurrentDictionary<int, HashSet<int>> g_in { get; }
        ConcurrentDictionary<int, HashSet<int>> g_out { get; }

        public void add(int from, int to)
        {
            g_out[from].Add(to);
            g_out[to].Add(from);

            g_in[to].Add(from);
            g_in[from].Add(to);
        }

        public Graph(int vertices)
        {
            this.vertices = vertices;
            g_in = new ConcurrentDictionary<int, HashSet<int>>();
            g_out = new ConcurrentDictionary<int, HashSet<int>>();

            for (int i = 0; i < vertices; i++)
            {
                g_in[i] = new HashSet<int>();
                g_out[i] = new HashSet<int>();
            }
        }


        async Task<List<int>> HamiltonianCycleAuxP(List<int> path, HashSet<int> set, int pos)
        {
            if (pos == vertices)
            {
                if (g_out[path[pos - 1]].Contains(path[0]))
                    return path;
                else
                    return null;
            }

            List<List<int>> results = new List<List<int>>();
            for (int i = 1; i < vertices; i++)
            {
                if (!set.Contains(i) && g_out[path[pos - 1]].Contains(i))
                {
                    List<int> pathClone = new List<int>(vertices);
                    pathClone.AddRange(path);
                    pathClone.Add(i);
                    HashSet<int> setClone = new HashSet<int>(set);
                    setClone.Add(i);
                    results.Add(await HamiltonianCycleAuxP(pathClone, setClone, pos + 1));
                }
            }
            return results.FirstOrDefault(list => list != null);
        }

        public List<int> HamiltonianCycleParallel()
        {

            var watch = System.Diagnostics.Stopwatch.StartNew();

            var l = new List<Task<List<int>>>();

            for (int i = 0; i < vertices; i++)
            {
                HashSet<int> set = new HashSet<int>();
                List<int> path = new List<int>();
                path.Add(i);
                set.Add(i);
                l.Add(HamiltonianCycleAuxP(path, set, 1));
            }

            bool finished = false;
            while (!finished)
            {
                finished = true;
                foreach (Task<List<int>> t in l)
                {
                    finished = finished && t.IsCompleted;
                    if (t.IsCompleted && t.Result != null)
                    {
                        watch.Stop();
                        var elapsed = watch.ElapsedMilliseconds;
                        Console.WriteLine($"Parallel Elapsed time: {elapsed} ms");
                        return t.Result;
                    }
                }
            }
            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine($"Parallel Elapsed time: {elapsedMs} ms");

            //var res = await Task.WhenAll(l);

            //watch.Stop();
            //var elapsedMs = watch.ElapsedMilliseconds;
            //Console.WriteLine($"Parallel Elapsed time: {elapsedMs} ms");

            //return res.FirstOrDefault(r => r != null);
            return null;
        }

        List<int> HamiltonianCycleAuxSeq(List<int> path, HashSet<int> set, int pos)
        {
            if (pos == vertices)
            {
                if (g_out[path[pos - 1]].Contains(path[0]))
                    return path;
                else
                    return null;
            }

            for (int i = 1; i < vertices; i++)
            {
                if (!set.Contains(i) && g_out[path[pos - 1]].Contains(i))
                {
                    path.Add(i);
                    set.Add(i);
                    var res = HamiltonianCycleAuxSeq(path, set, pos + 1);
                    if (res != null) return res;
                    else
                    {
                        set.Remove(i);
                        path.RemoveAt(path.Count - 1);
                    }
                }
            }
            return null;
        }
        public List<int> HamiltonianCycleSequential()
        {
            HashSet<int> set = new HashSet<int>();
            List<int> path = new List<int>();

            path.Add(0);
            set.Add(0);

            var watch = System.Diagnostics.Stopwatch.StartNew();

            var res = HamiltonianCycleAuxSeq(path, set, 1);

            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine($"Sequential Elapsed time: {elapsedMs} ms");

            return res;
        }
    }


    class Program
    {
        static Graph RandomGraph(int v, int n)
        {
            Graph g = new Graph(v);

            Random random = new Random();
            for (int i = 0; i < n; i++)
            {
                g.add(random.Next(0, v), random.Next(0, v));
            }
            return g;
        }
        static void Main(string[] args)
        {
            //Graph g = new Graph(5);

            //g.add(0, 1);
            //g.add(1, 2);
            //g.add(2, 4);
            //g.add(4, 3);
            //g.add(3, 0);
            //g.add(3, 1);
            //g.add(1, 4);

            Graph g = RandomGraph(20, 40);

            var k = g.HamiltonianCycleSequential();
            if (k != null)
            {
                Console.WriteLine(String.Join(' ', k));
            }
            else
            {
                Console.WriteLine("No hamiltonian cycle found");
            }

            var l = g.HamiltonianCycleParallel();
            if (l != null)
            {
                Console.WriteLine(String.Join(' ', l));
            }
            else
            {
                Console.WriteLine("No hamiltonian cycle found");
            }
        }
    }
}
