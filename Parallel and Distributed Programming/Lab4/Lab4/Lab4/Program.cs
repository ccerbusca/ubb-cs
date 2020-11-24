using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Lab4
{


    class Program
    {

        static void run_awaits(string[] hosts)
        {
            List<Task> tasks = new List<Task>();

            var i = 0;
            foreach (var host in hosts)
            {
                PageReader.Execute(host, 80, (Socket s) => {
                    tasks.Add(new Await(s, (string res) =>
                    {
                        System.IO.File.WriteAllText(host + i++ + ".txt", res);
                        Console.WriteLine(res);
                    }).readPage());
                });
            }

            Task.WaitAll(tasks.ToArray());
        }

        static void run_tasks(string[] hosts)
        {
            CountdownEvent cde = new CountdownEvent(hosts.Length);

            var i = 0;
            foreach (var host in hosts)
            {
                PageReader.Execute(host, 80, (Socket s) => {
                    new Tasks(s, (string res) =>
                    {
                        System.IO.File.WriteAllText(host + i++ + ".txt", res);
                        Console.WriteLine(res);
                        cde.Signal();
                    }).readPage();
                });
            }

            cde.Wait();
        }

        static void run_callbacks(string[] hosts)
        {
            CountdownEvent cde = new CountdownEvent(hosts.Length);

            var i = 0;
            foreach (var host in hosts)
            {
                PageReader.Execute(host, 80, (Socket s) => {
                    new Tasks(s, (string res) =>
                    {
                        System.IO.File.WriteAllText(host + i++ + ".txt", res);
                        Console.WriteLine(res);
                        cde.Signal();
                    }).readPage();
                });
            }

            cde.Wait();
        }



        static void Main(string[] args)
        {
            string[] sites = { "www.google.ro", "www.google.ro", "www.cs.ubbcluj.ro" };

            run_callbacks(sites);

            Console.ReadLine();

        }
    }
}
