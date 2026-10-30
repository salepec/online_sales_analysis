from product import Product
from product_manager import ProductManager


# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 800, 5))
manager.add_product(Product("Phone", 400, 3))
manager.add_product(Product("Mouse", 20, 10))
manager.add_product(Product("Keyboard", 50, 7))

# Prikaz svih proizvoda
print("AVAILABLE PRODUCTS:")
manager.display_products()

# Prikaz ukupne vrednosti inventara
print("\nTOTAL INVENTORY VALUE:")
print(manager.total_inventory_value())