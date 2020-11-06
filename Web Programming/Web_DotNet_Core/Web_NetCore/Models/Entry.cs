using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Web_NetCore.Models
{
    public class Entry
    {
        public int Id { get; set; }
        public string Content { get; set; }
        public DateTime Created_at { get; set; }
        public string Title { get; set; }
        public int Author_id { get; set; }
    }
}