import pandas as pd
from login import AdminLogin

class Admin:
    def __init__(self, username, password, catalog):
        self.username = username
        self.password = password
        self.catalog = catalog

    def login(self):
        adminLogin = AdminLogin(self.username, self.password)
        return adminLogin.login()

    def add_product(self):
        product_name = input("Enter product name: ")
        product_category = input("Enter product category: ")

        try:
            product_price = float(input("Enter product price: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for price.")
            return

        new_product = {
            "id": len(self.catalog.products) + 1,
            "name": product_name,
            "category": product_category,
            "price": product_price
        }

        self.catalog.add_product(new_product)
        self._display_action_result("Product added successfully", new_product)

    def remove_product(self):
        try:
            product_id = int(input("Enter product ID to remove: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for product ID.")
            return

        if not any(p["id"] == product_id for p in self.catalog.products):
            print(f"Product with ID {product_id} not found.")
            return

        self.catalog.products = self.catalog.remove_product(product_id)
        print(f"Product with ID {product_id} removed successfully.")
        self.view_catalog()

    def view_catalog(self):
        if not self.catalog.products:
            print("The catalog is currently empty.")
        else:
            print("\nCurrent Product Catalog:")
            print(pd.DataFrame(self.catalog.products))

    def _display_action_result(self, message, product):
        print(f"\n{message}:\n{pd.DataFrame([product])}")
        self.view_catalog()
