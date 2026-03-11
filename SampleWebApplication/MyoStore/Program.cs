using Microsoft.EntityFrameworkCore;
using MyoStore.Data;
using MyoStore.Models;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

// SQLite veritabanı yapılandırması
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlite("Data Source=MyoStore.db"));

var app = builder.Build();

// Veritabanını oluştur (varsa yoksa)
using (var scope = app.Services.CreateScope())
{
    var context = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    context.Database.EnsureCreated();
    
        // Örnek verileri ekle (veritabanı boşsa)
        if (!context.Categories.Any())
        {
            // Kategoriler
            context.Categories.AddRange(
                new Category { Id = 1, Name = "Ceket", Description = "Spor ve Günlük Ceketler" },
                new Category { Id = 2, Name = "Pantolon", Description = "Kot, Klasik ve Sportif Pantolonlar" },
                new Category { Id = 3, Name = "Ayakkabı", Description = "Spor, Günlük ve Klasik Ayakkabılar" },
                new Category { Id = 4, Name = "Tişört", Description = "Spor ve Günlük Tişörtler" }
            );
            
            // Ürünler
            context.Products.AddRange(
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
            );
        
        context.SaveChanges();
    }
}

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseRouting();

app.UseAuthorization();

app.MapStaticAssets();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}")
    .WithStaticAssets();


app.Run();

