using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab5
{

    class Consumer
    {
        Polynomial.Builder builder = new Polynomial.Builder();

        public void add(int powerOfX, int n)
        {
            builder.of(powerOfX, n);
        }

        public Polynomial result()
        {
            return builder.build();
        }
    }

    class Polynomial
    {

        public ConcurrentDictionary<int, int> pol { get; set; }

        private Polynomial(ConcurrentDictionary<int, int> pol)
        {
            this.pol = pol;
        }

        public class Builder
        {
            ConcurrentDictionary<int, int> pol = new ConcurrentDictionary<int, int>();

            public Polynomial.Builder of(int powerOfX, int n)
            {

                pol.AddOrUpdate(powerOfX, n, (key, value) => value + n);
                return this;
            }

            public Polynomial build()
            {
                return new Polynomial(pol);
            }
        }

        public void print()
        {
            var str = pol.ToList().OrderBy(pair => pair.Key).Aggregate("", (acc, pair) => acc + $"{pair.Value} * X^{pair.Key} + ");
            Console.WriteLine(str.Substring(0, str.Length - 3));
        }
    }


    



    class Program
    {

        static void sequential(Polynomial p1, Polynomial p2)
        {
            Consumer c = new Consumer();


            var watch = System.Diagnostics.Stopwatch.StartNew();

            p1.pol.ToList()
                .SelectMany(pair1 => p2.pol.ToList()
                                            .Select(pair2 => new { First = pair1, Second = pair2 }))
                .ToList()
                .ForEach(pair =>
                {
                    var pwrX = pair.First.Key + pair.Second.Key;
                    var n = pair.First.Value * pair.Second.Value;
                    c.add(pwrX, n);
                });

            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;

            c.result().print();

            Console.WriteLine($"Sequential Elapsed time: {elapsedMs} ms");
        }

        static void parallel(Polynomial p1, Polynomial p2)
        {
            Polynomial.Builder builder = new Polynomial.Builder();

            List<Task> tasks = new List<Task>();

            var watch = System.Diagnostics.Stopwatch.StartNew();

            p1.pol.ToList()
                .SelectMany(pair1 => p2.pol.ToList()
                                            .Select(pair2 => new { First = pair1, Second = pair2 }))
                .ToList()
                .ForEach(pair =>
                {
                    tasks.Add(Task.Run(() =>
                    {
                        var pwrX = pair.First.Key + pair.Second.Key;
                        var n = pair.First.Value * pair.Second.Value;
                        builder.of(pwrX, n);
                    }));
                });


            Task.WaitAll(tasks.ToArray());

            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;

            builder.build().print();
            Console.WriteLine($"Parallel Elapsed time: {elapsedMs} ms");
        }



        static void Main(string[] args)
        {
            Polynomial p1 = new Polynomial.Builder()
                            .of(0, 1)
                            .of(1, 2)
                            .of(2, 3)
                            .of(3, 4)
                            .of(4, 5)
                            .of(5, 6)
                            .of(6, 7)
                            .build();
            Polynomial p2 = new Polynomial.Builder()
                            .of(1, 2)
                            .of(2, 3)
                            .of(3, 4)
                            .of(4, 5)
                            .of(5, 6)
                            .of(6, 7)
                            .build();

            sequential(p1, p2);
            parallel(p1, p2);

            Console.ReadKey();

        }
    }
}
