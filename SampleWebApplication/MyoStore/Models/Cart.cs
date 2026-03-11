namespace MyoStore.Models
{
    public class CartItem
    {
        public int Id { get; set; }
        public int ProductId { get; set; }
        public Product? Product { get; set; }
        public int Quantity { get; set; }
    }

    public class Cart
    {
        public List<CartItem> Items { get; set; } = new List<CartItem>();
        
        public decimal TotalPrice => Items.Sum(x => (x.Product?.Price ?? 0) * x.Quantity);
        public int TotalItemCount => Items.Sum(x => x.Quantity);
    }
}
