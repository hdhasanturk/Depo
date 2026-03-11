using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MyoStore.Data;
using MyoStore.Models;
using System.Text.Json;

namespace MyoStore.Controllers
{
    public class CartController : Controller
    {
        private readonly AppDbContext _context;

        public CartController(AppDbContext context)
        {
            _context = context;
        }

        private Cart GetCart()
        {
            var cartJson = HttpContext.Session.GetString("Cart");
            if (string.IsNullOrEmpty(cartJson))
            {
                return new Cart();
            }
            return JsonSerializer.Deserialize<Cart>(cartJson) ?? new Cart();
        }

        private void SaveCart(Cart cart)
        {
            HttpContext.Session.SetString("Cart", JsonSerializer.Serialize(cart));
        }

        public IActionResult Index()
        {
            var cart = GetCart();
            foreach (var item in cart.Items)
            {
                item.Product = _context.Products.Include(p => p.Category).FirstOrDefault(p => p.Id == item.ProductId);
            }
            return View(cart);
        }

        public IActionResult Add(int productId, int quantity = 1)
        {
            var cart = GetCart();
            var existingItem = cart.Items.FirstOrDefault(x => x.ProductId == productId);

            if (existingItem != null)
            {
                existingItem.Quantity += quantity;
            }
            else
            {
                cart.Items.Add(new CartItem
                {
                    ProductId = productId,
                    Quantity = quantity
                });
            }

            SaveCart(cart);
            TempData["Message"] = "Ürün sepete eklendi!";
            return RedirectToAction("Index");
        }

        public IActionResult Remove(int productId)
        {
            var cart = GetCart();
            var item = cart.Items.FirstOrDefault(x => x.ProductId == productId);
            
            if (item != null)
            {
                cart.Items.Remove(item);
                SaveCart(cart);
                TempData["Message"] = "Ürün sepetten kaldırıldı!";
            }

            return RedirectToAction("Index");
        }

        public IActionResult Update(int productId, int quantity)
        {
            var cart = GetCart();
            var item = cart.Items.FirstOrDefault(x => x.ProductId == productId);
            
            if (item != null)
            {
                if (quantity <= 0)
                {
                    cart.Items.Remove(item);
                }
                else
                {
                    item.Quantity = quantity;
                }
                SaveCart(cart);
            }

            return RedirectToAction("Index");
        }

        public IActionResult Clear()
        {
            SaveCart(new Cart());
            TempData["Message"] = "Sepet temizlendi!";
            return RedirectToAction("Index");
        }
    }
}
