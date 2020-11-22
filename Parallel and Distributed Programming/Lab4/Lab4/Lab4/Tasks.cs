using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace Lab4
{
    class Tasks
    {
        private readonly Socket s;
        private readonly Action<string> callback;
        private readonly Byte[] buffer = new byte[256];
        private string page = "";

        public Tasks(Socket s, Action<string> callback)
        {
            this.s = s;
            this.callback = callback;
        }

        public void readPage()
        {
            Task<int> future = Receive();
            future.ContinueWith((Task<int> f) => onBytesReceived(f));
        }

        private void onBytesReceived(Task<int> f)
        {
            int bytes = f.Result;
            page += Encoding.ASCII.GetString(buffer, 0, bytes);
            if (bytes > 0)
                Receive().ContinueWith(received => onBytesReceived(received));
            else
            {
                s.Close();
                s.Dispose();
                callback(page);
            }
        }

        private Task<int> Receive()
        {
            TaskCompletionSource<int> promise = new TaskCompletionSource<int>();
            s.BeginReceive(buffer, 0, buffer.Length, SocketFlags.None,
                (IAsyncResult ar) => promise.SetResult(s.EndReceive(ar)), null);
            return promise.Task;
        }

    }
}
