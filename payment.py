class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self, method):
        method = method.strip().lower()
        methods = {
            "upi": "UPI",
            "debit card": "Debit Card"
        }

        if method in methods:
            print(
                f"Payment of Rs. {self.amount} will be processed through {methods[method]}.")
        else:
            print(f"Unknown payment method. Please choose either 'UPI' or 'Debit Card'.")
