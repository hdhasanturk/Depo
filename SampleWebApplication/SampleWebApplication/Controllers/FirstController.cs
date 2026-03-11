using Microsoft.AspNetCore.Mvc;

namespace SampleWebApplication.Controllers
{
    public class FirstController : Controller
    {
        public IActionResult Index()
        {
            return View("Index2");
        }

        public IActionResult Index2()
        {
            return View();
        }
    }
}
