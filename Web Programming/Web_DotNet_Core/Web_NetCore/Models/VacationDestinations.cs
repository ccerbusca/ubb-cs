using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Web_NetCore.Models
{
    public class VacationDestinations
    {
        public int Id { get; set; }
        public string Destination { get; set; }
        public string Country { get; set; }
        public int Price { get; set; }
    }
}
