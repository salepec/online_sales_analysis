from product import Product
from product_manager import ProductManager
from cart import Cart
import random


# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 800, 5))
manager.add_product(Product("Phone", 400, 3))
manager.add_product(Product("Mouse", 20, 10))
manager.add_product(Product("Keyboard", 50, 7))


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