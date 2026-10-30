from product import Product
from product_manager import ProductManager

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Gaming Laptop", 900, 4))
manager.add_product(Product("Smartphone", 500, 5))
manager.add_product(Product("Wireless Mouse", 25, 12))
manager.add_product(Product("Mechanical Keyboard", 70, 6))