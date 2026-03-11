using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyoStore.Data;
using MyoStore.Models;

namespace MyoStore.Controllers
{
    public class ProductController : Controller
    {
        private readonly AppDbContext _context;

        public ProductController(AppDbContext context)
        {
            _context = context;
        }

        public IActionResult Index(int? categoryId)
        {
            IQueryable<Product> products = _context.Products.Include(p => p.Category);
            
            if (categoryId.HasValue && categoryId > 0)
            {
                products = products.Where(p => p.CategoryId == categoryId);
            }

            ViewBag.Categories = _context.Categories.ToList();
            ViewBag.SelectedCategory = categoryId;
            
            return View(products.ToList());
        }

        public IActionResult Details(int id)
        {
            var product = _context.Products.Include(p => p.Category).FirstOrDefault(p => p.Id == id);
            if (product == null)
            {
                return NotFound();
            }
            
            return View(product);
        }

        public IActionResult Search(string query)
        {
            var products = _context.Products
                .Include(p => p.Category)
                .Where(p => p.Name.Contains(query, StringComparison.OrdinalIgnoreCase) || 
                           p.Description.Contains(query, StringComparison.OrdinalIgnoreCase))
                .ToList();

            ViewBag.Query = query;
            return View(products);
        }
    }
}
