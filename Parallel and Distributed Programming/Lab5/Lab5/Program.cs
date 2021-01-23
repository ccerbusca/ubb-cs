using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Lab5
{

    class Polynomial
    {

        public List<int> polynomial { get; set;}

        private Polynomial(List<int> pol)
        {
            this.polynomial = pol;
        }

        public class Builder
        {

            object mtx = new object();
            int degree = -1;
            ConcurrentDictionary<int, int> pol = new ConcurrentDictionary<int, int>();

            public Polynomial.Builder of(int powerOfX, int n)
            {
                lock(mtx)
                {
                    if (powerOfX > degree)
                    {
                        degree = powerOfX;
                    }
                }
                pol.AddOrUpdate(powerOfX, n, (key, value) => value + n);
                return this;
            }

            public Polynomial.Builder from(List<int> l)
            {
                int i = 0;
                l.ForEach(e =>
                {
                    lock (mtx)
                    {
                        if (i > degree)
                        {
                            degree = i;
                        }
                    }
                    pol.AddOrUpdate(i, e, (key, value) => value + i);
                    Interlocked.Increment(ref i);
                });
                return this;
            }

            public Polynomial build()
            {
                List<int> r = Enumerable.Repeat(0, degree + 1).ToList();
                pol.ToList().ForEach(pair => r[pair.Key] = pair.Value);
                return new Polynomial(r);
            }
        }

        public void print()
        {
            var str = polynomial.Zip(Enumerable.Range(0, polynomial.Count), (a, b) => new { val = a, power = b } ).Where(e => e.val != 0).Aggregate("", (acc, e) => acc + $"{e.val} * X^{e.power} + ");
            Console.WriteLine(str.Substring(0, str.Length - 3));
        }
    }


    



    class Program
    {

        static void sequential(Polynomial p1, Polynomial p2)
        {
            Polynomial.Builder builder = new Polynomial.Builder();


            var watch = System.Diagnostics.Stopwatch.StartNew();

            p1.polynomial
                .Zip(Enumerable.Range(0, p1.polynomial.Count), (a, b) => new { val = a, power = b })
                .SelectMany(pair1 => p2.polynomial
                                            .Zip(Enumerable.Range(0, p2.polynomial.Count), (a, b) => new { val = a, power = b })
                                            .Select(pair2 => new { First = pair1, Second = pair2 }))
                .ToList()
                .ForEach(pair =>
                {
                    var pwrX = pair.First.power + pair.Second.power;
                    var n = pair.First.val * pair.Second.val;
                    builder.of(pwrX, n);
                });

            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;

           //builder.build().print();

           Console.WriteLine($"Sequential Elapsed time: {elapsedMs} ms");
        }


        static async Task parallel_helper(List<int> p1, List<int> p2, int i, Polynomial.Builder builder)
        {
            for (int j = 0; j < p2.Count; j++)
            {
                var pwrX = i + j;
                var n = p1[i] * p2[j];
                builder.of(pwrX, n);
            }
        }


        static async Task parallel(Polynomial p1, Polynomial p2)
        {
            Polynomial.Builder builder = new Polynomial.Builder();


            var watch = System.Diagnostics.Stopwatch.StartNew();

            for (int i = 0; i < p1.polynomial.Count; i++)
            {
                await parallel_helper(p1.polynomial, p2.polynomial, i, builder);
            }


            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;

            //builder.build().print();
            Console.WriteLine($"Parallel Elapsed time: {elapsedMs} ms");
        }

        static List<int> addPolynomials(List<int> a, List<int> b)
        {
            resize(ref a, ref b);
            return a.Zip(b, (a1, b1) => a1 + b1).ToList();
        }

        static List<int> minusPoly(List<int> a, List<int> b)
        {
            return a.Zip(b, (a1, b1) => a1 - b1).ToList();
        }

        static void resize(ref List<int> p1, ref List<int> p2)
        {
            if (p1.Count < p2.Count)
            {
                p1 = p1.Concat(Enumerable.Repeat(0, p2.Count - p1.Count)).ToList();
            }
            else if (p2.Count < p1.Count)
            {
                p2 = p2.Concat(Enumerable.Repeat(0, p1.Count - p2.Count)).ToList();
            }
        }


        static List<int> karatsuba_aux(List<int> p1, List<int> p2)
        {

            resize(ref p1, ref p2);

            if (p2.Count == 1)
            {
                List<int> res = new List<int>(1);
                res.Add(p1[0] * p2[0]);
                return res;
            }


            List<int> p1L = p1.Take(p1.Count / 2).ToList();
            List<int> p1R = p1.Skip(p1.Count / 2).ToList();
            List<int> p2L = p2.Take(p2.Count / 2).ToList();
            List<int> p2R = p2.Skip(p2.Count / 2).ToList();



            List<int> r1 = karatsuba_aux(p1L, p2L);
            List<int> r2 = karatsuba_aux(p1R, p2R);
            List<int> r3 = karatsuba_aux(addPolynomials(p1L, p1R), addPolynomials(p2L, p2R));

            List<int> middle = minusPoly(minusPoly(r3, r1), r2);

            return r1.Concat(middle).Concat(r2).ToList();
        }

        static void seq_karatsuba(Polynomial p1, Polynomial p2)
        {
            Polynomial.Builder builder = new Polynomial.Builder();

            var watch = System.Diagnostics.Stopwatch.StartNew();

            var res = karatsuba_aux(p1.polynomial, p2.polynomial);


            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;

            //builder.from(res).build().print();

            Console.WriteLine($"Sequential Karatsuba Elapsed time: {elapsedMs} ms");
        }

        static async Task<List<int>> karatsuba_aux_par(List<int> p1, List<int> p2)
        {
            resize(ref p1, ref p2);

            if (p2.Count == 1)
            {
                List<int> res = new List<int>(1);
                res.Add(p1[0] * p2[0]);
                return res;
            }


            List<int> p1L = p1.Take(p1.Count / 2).ToList();
            List<int> p1R = p1.Skip(p1.Count / 2).ToList();
            List<int> p2L = p2.Take(p2.Count / 2).ToList();
            List<int> p2R = p2.Skip(p2.Count / 2).ToList();



            List<int> r1 = await karatsuba_aux_par(p1L, p2L);
            List<int> r2 = await karatsuba_aux_par(p1R, p2R);
            List<int> r3 = await karatsuba_aux_par(addPolynomials(p1L, p1R), addPolynomials(p2L, p2R));

            List<int> middle = minusPoly(minusPoly(r3, r1), r2);

            return r1.Concat(middle).Concat(r2).ToList();
        }

        static void parallel_karatsuba(Polynomial p1, Polynomial p2)
        {
            Polynomial.Builder builder = new Polynomial.Builder();

            var watch = System.Diagnostics.Stopwatch.StartNew();

            var res = karatsuba_aux_par(p1.polynomial, p2.polynomial).Result;


            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;

           // builder.from(res).build().print();

            Console.WriteLine($"Parallel Karatsuba Elapsed time: {elapsedMs} ms");
        }



        static void Main(string[] args)
        {
            //Polynomial p1 = new Polynomial.Builder()
            //                .of(0, 5)
            //                .of(1, 0)
            //                .of(2, 10)
            //                .of(3, 6)
            //                .of(4, 1)
            //                .build();
            //Polynomial p2 = new Polynomial.Builder()
            //                .of(0, 1)
            //                .of(1, 2)
            //                .of(2, 4)
            //                .build();
            var b1 = new Polynomial.Builder();
            var b2 = new Polynomial.Builder();
            for (int i = 0; i < 250; i++)
            {
                b1.of(i, i + 1);
                b2.of(i, 2 * i + 1);
            }

            Polynomial p1 = b1.build();
            Polynomial p2 = b2.build();

            sequential(p1, p2);
            parallel(p1, p2);

            seq_karatsuba(p1, p2);
            parallel_karatsuba(p1, p2);

            Console.ReadKey();

        }
    }
}
