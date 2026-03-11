using MyoStore.Models;

namespace MyoStore.Data
{
    public static class FakeData
    {
        public static List<Category> Categories = new List<Category>
        {
            new Category { Id = 1, Name = "Ceket", Description = "Spor ve Günlük Ceketler" },
            new Category { Id = 2, Name = "Pantolon", Description = "Kot, Klasik ve Sportif Pantolonlar" },
            new Category { Id = 3, Name = "Ayakkabı", Description = "Spor, Günlük ve Klasik Ayakkabılar" },
            new Category { Id = 4, Name = "Tişört", Description = "Spor ve Günlük Tişörtler" }
        };

        public static List<Product> Products = new List<Product>
        {
            new Product { Id = 1, Name = "Spor Ceket", Description = "Siyah Renk, Mavi Kot", Price = 1500, Stock = 50, CategoryId = 1 },
            new Product { Id = 2, Name = "Deri Ceket", Description = "Kahverengi Deri, Şişme", Price = 3500, Stock = 20, CategoryId = 1 },
            new Product { Id = 3, Name = "Mont", Description = "Yeşil, Kaban Tipi", Price = 2500, Stock = 30, CategoryId = 1 },
            
            new Product { Id = 4, Name = "Kot Pantolon", Description = "Mavi, Bilek Geniş", Price = 800, Stock = 100, CategoryId = 2 },
            new Product { Id = 5, Name = "Klasik Pantolon", Description = "Siyah, Düz", Price = 600, Stock = 75, CategoryId = 2 },
            new Product { Id = 6, Name = "Sportif Pantolon", Description = "Gri, Eşofman", Price = 400, Stock = 60, CategoryId = 2 },
            
            new Product { Id = 7, Name = "Spor Ayakkabı", Description = "Beyaz, Nike", Price = 2500, Stock = 40, CategoryId = 3 },
            new Product { Id = 8, Name = "Günlük Ayakkabı", Description = "Siyah, Topuklu", Price = 1800, Stock = 35, CategoryId = 3 },
            new Product { Id = 9, Name = "Klasik Ayakkabı", Description = "Kahverengi, Deri", Price = 3000, Stock = 25, CategoryId = 3 },
            
            new Product { Id = 10, Name = "Spor Tişört", Description = "Beyaz, Dri-Fit", Price = 350, Stock = 100, CategoryId = 4 },
            new Product { Id = 11, Name = "Basic Tişört", Description = "Siyah, Pamuklu", Price = 250, Stock = 150, CategoryId = 4 },
            new Product { Id = 12, Name = "Desenli Tişört", Description = "Mavi, Çizgili", Price = 450, Stock = 80, CategoryId = 4 }
        };

        public static List<Product> GetProductsByCategory(int categoryId)
        {
            return Products.Where(p => p.CategoryId == categoryId).ToList();
        }

        public static Product? GetProductById(int id)
        {
            return Products.FirstOrDefault(p => p.Id == id);
        }
    }
}
