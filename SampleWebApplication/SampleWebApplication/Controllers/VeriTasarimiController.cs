using Microsoft.AspNetCore.Mvc;
using SampleWebApplication.Data;

namespace SampleWebApplication.Controllers
{
    public class VeriTasarimiController : Controller
    {
        public IActionResult Yontem1()
        {
            ViewData["metin"] = "Bugun hava çok güzel";//returnden önce yazılır
            ViewData["sayi"] = 20;
            return View();
        }
        public IActionResult Yontem2()
        {

            //returnden önce yazılır
            ViewBag.metin = "Bugun hava çok kötü";
            ViewBag.sayi = 10;
            ViewBag.mantiksaldeger = true;
            return View();


        }

        public IActionResult Yontem3() 
        {

            var myPerson=FakeData.people.FirstOrDefault();
            return View(myPerson);


        }
    }
}
