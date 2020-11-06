using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Web_NetCore.Models
{
    public class Order
    {
        public int Id { get; set; }
        public string User { get; set; }
        public int ProductId { get; set; }
        public int Quantity { get; set; }
    }
}
