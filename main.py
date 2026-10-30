
from product import Product
from product_manager import ProductManager
from cart import Cart
import random

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Gaming Laptop", 900, 4))
manager.add_product(Product("Smartphone", 500, 5))
manager.add_product(Product("Wireless Mouse", 25, 12))
manager.add_product(Product("Mechanical Keyboard", 70, 6))

# Kreiranje instance Cart
cart = Cart()

# Nasumičan izbor tri proizvoda
selected_products = random.sample(manager.products, 3)

# Dodavanje proizvoda u korpu
for product in selected_products:
    cart.add_to_cart(product)

# Prikaz sadržaja korpe
print("SHOPPING CART:")
cart.display_cart()

# Prikaz ukupne vrednosti korpe
print("\nTOTAL TO PAY:")
print(cart.calculate_total())
