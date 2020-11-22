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
        static void Main(string[] args)
        {
            CountdownEvent cde = new CountdownEvent(1);

            PageReader.Execute("www.cs.ubbcluj.ro", 80, (Socket s) => {
                new Await(s, (string res) => {
                    Console.WriteLine(res);
                    cde.Signal();
                }).readPage().Wait();
            });

            cde.Wait();

            Console.ReadLine();

        }
    }
}
