// Product list with 9 images
const PRODUCTS = [
    { id: 1, name: "Watch 1", price: 199.99, image: "product 1.jpg", description: "Stylish premium watch." },
    { id: 2, name: "Watch 2", price: 219.99, image: "product 2.jpg", description: "Elegant design." },
    { id: 3, name: "Watch 3", price: 249.99, image: "product 3.jpg", description: "Water resistant." },
    { id: 4, name: "Watch 4", price: 279.99, image: "product 4.jpg", description: "Premium metal body." },
    { id: 5, name: "Watch 5", price: 299.99, image: "product 5.jpg", description: "Stainless steel." },
    { id: 6, name: "Watch 6", price: 329.99, image: "product 6.jpg", description: "High accuracy quartz." },
    { id: 7, name: "Watch 7", price: 349.99, image: "product 7.jpg", description: "Golden finish." },
    { id: 8, name: "Watch 8", price: 379.99, image: "product 8.jpg", description: "Sporty and bold." },
    { id: 9, name: "Watch 9", price: 399.99, image: "product 9.jpg", description: "Elegant design. " },
    { id: 10, name: "Watch 10", price: 450.99, image: "product 10.jpg", description: "Stylish premium watch." },
    { id: 11, name: "Watch 11", price: 500.99, image: "product 11.jpg", description: "Premium metal body" },
    { id: 12, name: "Watch 12", price: 600.99, image: "product 12.jpg", description: "Golden finish." }



];

// Fetch all products
async function fetchProducts() {
    return PRODUCTS;
}

// Fetch specific product
async function fetchProduct(id) {
    let p = PRODUCTS.find(item => item.id == id);
    if (!p) throw new Error("Product not found");
    return p;
}

// Image URL from same folder
function productImageUrl(product) {
    return product.image;  // direct image filename
}

// Get cart
function getCart() {
    return JSON.parse(localStorage.getItem("cart") || "[]");
}

// Clear cart
function clearCart() {
    localStorage.removeItem("cart");
}

// Fake order submit function
async function submitOrder(data) {

    let total = 0;
    for (let item of data.cart) {
        let p = PRODUCTS.find(prod => prod.id == item.id);
        if (p) total += p.price * item.qty;
    }

    // Fake API response (acts like a real server)
    return {
        success: true,
        order_id: "ORD" + Math.floor(Math.random() * 90000 + 10000),
        total: total
    };
}

// Add to cart (localStorage)
function addToCart(id, qty) {
    let cart = JSON.parse(localStorage.getItem("cart") || "[]");
    let existing = cart.find(item => item.id == id);

    if (existing) existing.qty += qty;
    else cart.push({ id, qty });

    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Added to cart!");
}
