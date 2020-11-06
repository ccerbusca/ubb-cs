using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Web_NetCore.Models
{
    public class BannedList
    {
        public int Id { get; set; }
        public string User { get; set; }
        public int DestinationID { get; set; }
    }
}
