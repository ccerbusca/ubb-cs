using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Web_NetCore.Models
{
    public class User
    {
        public int Id { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
        public bool Admin { get; set; }
        public DateTime Created_at { get; set; }
    }
}