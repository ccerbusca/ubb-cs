using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace Lab4
{
    class Callbacks
    {
        Socket s;
        string page = "";
        Byte[] bytesReceived = new Byte[256];
        Action<string> callback;


        public Callbacks(Socket s, Action<string> callback)
        {
            this.s = s;
            this.callback = callback;
        }

        public void readPage()
        {
            s.BeginReceive(bytesReceived, 0, bytesReceived.Length, SocketFlags.None, onBytesReceived, null);
        }

        void onBytesReceived(IAsyncResult ar)
        {
            int bytes = s.EndReceive(ar);
            page += Encoding.ASCII.GetString(bytesReceived, 0, bytes);
            if (bytes > 0)
                s.BeginReceive(bytesReceived, 0, bytesReceived.Length, SocketFlags.None, onBytesReceived, null);
            else
            {
                s.Close();
                s.Dispose();
                callback(page);
            }
        }
    }
}
