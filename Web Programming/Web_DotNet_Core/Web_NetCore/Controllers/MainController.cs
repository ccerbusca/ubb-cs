using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using Web_NetCore.Data;
using Web_NetCore.Models;

/*
 * [HttpGet]
        public string GetEntries([Range(1, 30)]int page = 1)
        {
            string result = "<table class=\"table\"><thead><tr><th>Content</th><th>Created at</th><th>Title</th><th>Author</th><th></th><tr></thead><tbody>";

            List<Entry> entries = ModelState.IsValid ? GetEntriesPaged(page) : GetEntriesPaged(1);

            foreach (Entry entry in entries)
            {
                User user = context.Users.Where(u => u.Id == entry.Author_id).Select(u => new User { Email = u.Email }).FirstOrDefault();
                result += "<tr><td>" + entry.Content + "</td><td>" + entry.Created_at.ToString() + "</td><td>" + entry.Title + "</td><td>" + user.Email + "</td><td>"+ DeleteButton(entry.Id) + "</td></tr>";
            }

            result += "</tbody></table>";
            return result;
        }

        [HttpPost]
        public string GetEntriesFiltered(FilterForm form, [Range(1, 30)] int page = 1)
        {
            string result = "<table class=\"table\"><thead><tr><th>Content</th><th>Created at</th><th>Title</th><th>Author</th><th></th><tr></thead><tbody>";

            List<Entry> entries = ModelState.IsValid ? GetEntriesPagedFiltered(page, form) : GetEntriesPagedFiltered(1, form);

            foreach (Entry entry in entries)
            {
                User user = context.Users.Where(u => u.Id == entry.Author_id).Select(u => new User { Email = u.Email }).FirstOrDefault();
                result += "<tr><td>" + entry.Content + "</td><td>" + entry.Created_at.ToString() + "</td><td>" + entry.Title + "</td><td>" + user.Email + "</td><td>" + DeleteButton(entry.Id) + "</td></tr>";
            }

            result += "</tbody></table>";
            return result;
        }

        public ActionResult Entries()
        {
            return View("Entries");
        }

        private string DeleteButton(int id)
        {
            if (session.GetString("admin") == "yep")
                return "<a href=\"/DeleteEntry/"+ id.ToString() + "\">Delete</a>";
            return "";
        }

        [Route("/DeleteEntry/{id}")]
        public ActionResult DeleteEntry(int id)
        {
            var entry = new Entry { Id = id };
            context.Entries.Attach(entry);
            context.Entries.Remove(entry);
            context.SaveChanges();
            return new RedirectToActionResult("Entries", "Main", new { });
        }

        [HttpPost]
        public ActionResult AddEntry(EntryForm entry)
        {
            User user = context.Users.Where(u => u.Email == session.GetString("email")).Select(u => new User { Id = u.Id }).FirstOrDefault();
            context.Entries.Add(new Entry { Content = entry.Content, Title = entry.Title, Author_id = user.Id, Created_at= DateTime.Now});
            context.SaveChanges();
            return new RedirectToActionResult("Entries", "Main", new { });
        }

        public ActionResult Logout()
        {
            session.Clear();
            return new RedirectToActionResult("Login", "Main", new { });
        }

        public ActionResult Register()
        {
            return View("Register");
        }

        public ActionResult Login()
        {
            return View("Login");
        }

        [HttpPost]
        public ActionResult HandleRegister(UserForm user)
        {
            if (ModelState.IsValid)
            {
                if (context.Users.Where(u => u.Email == user.Email).Count() == 0)
                {
                    context.Users.Add(new User { Admin = false, Email = user.Email, Password = user.Password });
                    context.SaveChanges();
                    return View("Login");
                }
                else
                {
                    ModelState.AddModelError("Email", "Email already used");
                    return View("Register", user);
                }
            }
            else
            {
                return View("Register", user);
            }
        }

        [HttpPost]
        public ActionResult HandleLogin(UserForm user)
        {
            if (ModelState.IsValid)
            {
                var fetched = context.Users.Where(u => u.Email == user.Email).Select(u => new User { Email = u.Email, Password = u.Password, Admin = u.Admin, Id = u.Id }).FirstOrDefault();
                if (fetched != null && fetched.Email == user.Email)
                {
                    if (fetched.Password == user.Password)
                    {
                        session.SetString("logged", "yep");
                        session.SetString("email", fetched.Email);
                        session.SetString("admin", fetched.Admin ? "yep" : "nop");
                        return new RedirectToActionResult("Entries", "Main", new { });
                    }
                    else
                    {
                        ModelState.AddModelError("Password", "Wrong password");
                        return View("Login", user);
                    }
                }
                else
                {
                    ModelState.AddModelError("Email", "Email not registered to any account");
                    return View("Login", user);
                }
            }
            else
            {
                return View("Login", user);
            }
        }

        private List<Entry> GetEntriesPaged(int page)
        {
            return context.Entries.OrderByDescending(e => e.Created_at).Skip((page - 1) * 4).Take(4).ToList();
        }

        private List<Entry> GetEntriesPagedFiltered(int page, FilterForm form)
        {
            List<int> id = new List<int>();
            if (form.Email != null && form.Email.Length != 0) {
                id = context.Users.Where(u => u.Email.Contains(form.Email)).Select(u => u.Id).ToList();
            }
            if (form.Title == null || form.Title.Length == 0)
                form.Title = "";
            return context.Entries
                .Where(e => e.Title.Contains(form.Title) && (id.Count() > 0 ? id.Contains(e.Author_id) : true))
                .OrderByDescending(e => e.Created_at).Skip((page - 1) * 4).Take(4).ToList();
        }
    }
 */

namespace Web_NetCore.Controllers
{
    public class MainController : Controller
    {
        private readonly DBWpContext context;
        private readonly ISession session;

        public MainController(DBWpContext wpContext, IHttpContextAccessor httpContextAccessor)
        {
            this.context = wpContext;
            this.session = httpContextAccessor.HttpContext.Session;
        }

        public IActionResult Index()
        {
            return View();
        }

        public ActionResult LoginPage()
        {
            session.SetString("saved", "");
            return View("Login");
        }

        public ActionResult Login(string user)
        {
            session.SetString("user", user);
            return Destinations();
        }

        public ActionResult Destinations()
        {
            return View("Destinations");
        }
        [HttpPost]
        public ActionResult AddBannedList(BannedList bannedList)
        {
            context.BannedList.Add(new BannedList { DestinationID = bannedList.DestinationID, User = session.GetString("user") });
            context.SaveChanges();
            return View("Destinations");
        }

        [HttpGet]
        public string FilterDestinations(string q)
        {
            string result = "<table class=\"table\"><thead><tr><th>id</th><th>destination</th><th>country</th><th>price</th><tr></thead><tbody>";

            if (q == null)
                q = "";

            List<int> bannedList = context.BannedList.Where(bl => bl.User == session.GetString("user")).Select(bl => bl.DestinationID).ToList();
            List<VacationDestinations> destinations = context.VacationDestinations.Where(vd => !bannedList.Contains(vd.Id) && vd.Destination.Contains(q)).ToList();

            foreach (var d in destinations)
            {
                result += "<tr><td>" + d.Id.ToString() + "</td><td>" + d.Destination + "</td><td>" + d.Country + "</td><td>" + d.Price + "</td></tr>";
            }

            result += "</tbody></table>";
            return result;
        }

        [HttpGet]
        public ActionResult FilterDestinationsJson(string q)
        {
            if (q == null)
                q = "";

            List<int> bannedList = context.BannedList.Where(bl => bl.User == session.GetString("user")).Select(bl => bl.DestinationID).ToList();
            List<VacationDestinations> destinations = context.VacationDestinations.Where(vd => !bannedList.Contains(vd.Id) && vd.Destination.Contains(q)).ToList();
            return Json(destinations);
        }

    }
}
