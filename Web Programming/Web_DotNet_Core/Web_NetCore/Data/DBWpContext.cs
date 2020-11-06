using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Web_NetCore.Models;

namespace Web_NetCore.Data
{
    public class DBWpContext : DbContext
    {
        public DBWpContext(DbContextOptions options) : base(options) { }

        public DbSet<BannedList> BannedList { get; set; }
        public DbSet<VacationDestinations> VacationDestinations { get; set; }
    }
}
