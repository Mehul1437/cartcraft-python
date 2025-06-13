import pandas as pd
from utils.db_mock import load_data, save_data


class Catalog:
    def __init__(self):
        self.products = load_data("products")
        self._update_categories()

    def _update_categories(self):
        self.categories = list({product["category"]
                               for product in self.products})

    def add_product(self, product):
        self.products.append(product)
        save_data("products",self.products)
        self._update_categories()
        print("✅ Product added and saved.")

    def remove_product(self, product_id):
        original_len = len(self.products)
        self.products = [p for p in self.products if p["id"] != product_id]
        if len(self.products) < original_len:
            save_data("products",self.products)
            self._update_categories()
            print("🗑️ Product removed and saved.")
        else:
            print(f"⚠️ Product with ID {product_id} not found.")

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories.append(category_name)
            print(f"📁 Category '{category_name}' added.")
        else:
            print(f"⚠️ Category '{category_name}' already exists.")

    def remove_category(self, category_name):
        if category_name in self.categories:
            self.categories.remove(category_name)
            print(f"🗑️ Category '{category_name}' removed.")
        else:
            print(f"⚠️ Category '{category_name}' not found.")

    def view_products(self):
        return pd.DataFrame(self.products)

    def __str__(self):
        df = self.view_products()
        return df.to_string(index=False) if not df.empty else "🛒 The catalog is empty."
