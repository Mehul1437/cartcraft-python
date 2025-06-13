class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        for item in self.cart_items:
            if item["product"]["id"] == product["id"]:
                item["quantity"] += quantity
                return
        self.cart_items.append({"product": product, "quantity": quantity})

    def remove_from_cart(self, product_id):
        original_len = len(self.cart_items)
        self.cart_items = [
            item for item in self.cart_items if item["product"]["id"] != product_id]
        if len(self.cart_items) == original_len:
            print(f"Product with ID {product_id} not found in cart.")

    def view_cart(self):
        return self.cart_items

    def __str__(self):
        if not self.cart_items:
            return "Your cart is empty."
        return "\n".join(
            f'{item["product"]["name"]} (x{item["quantity"]}) - ${item["product"]["price"]:.2f}'
            for item in self.cart_items
        )
