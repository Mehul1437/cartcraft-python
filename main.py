from admin import Admin
from cart import Cart
from catalog import Catalog
from login import User
from payment import Payment
from utils.db_mock import users_db, save_data


def admin_page(catalog):
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    admin = Admin(username, password, catalog)

    if not admin.login():
        print("Invalid admin credentials.")
        return

    print("Admin login successful!")
    while True:
        print("\nAdmin actions:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Catalog")
        print("4. View Users")
        print("5. Remove User")
        print("6. Exit")

        choice = input("Choose an action (1-6): ").strip()

        if choice == '1':
            admin.add_product()
        elif choice == '2':
            admin.remove_product()
        elif choice == '3':
            admin.view_catalog()
        elif choice == '4':
            print("\nRegistered Users:")
            for username, password in users_db.items():
                print(f"Username: {username}, Password: {password}")
        elif choice == '5':
            username_to_remove = input("Enter the username to remove: ")
            if username_to_remove in users_db:
                del users_db[username_to_remove]
                save_data("users",users_db)
                print(f"User '{username_to_remove}' has been removed.")
            else:
                print(f"User '{username_to_remove}' not found.")
        elif choice == '6':
            print("Exiting admin page...")
            break
        else:
            print("Invalid choice. Please try again.")


def handle_user_flow(username):
    catalog = Catalog()
    cart = Cart()

    print("\nCatalog:")
    product_list = catalog.view_products().to_dict(orient='records')
    for product in product_list:
        print(
            f"{product['id']}: {product['name']} - Rs. {product['price']} ({product['category']})")

    try:
        product_id = int(input("\nEnter product ID to add to cart: "))
        quantity = int(input("Enter quantity to add: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    product = next((p for p in product_list if p["id"] == product_id), None)
    if not product:
        print("Product not found.")
        return

    cart.add_to_cart(product, quantity)
    print(f"{product['name']} added to cart.")

    print("\nYour Cart:")
    for item in cart.view_cart():
        total = item['product']['price'] * item['quantity']
        print(f"{item['product']['name']} x{item['quantity']} - Rs. {total}")

    total_amount = sum(item['product']['price'] * item['quantity']
                       for item in cart.view_cart())
    print(f"\nTotal amount to be paid: Rs. {total_amount}")

    payment_method = input("Choose payment method (UPI/Debit Card): ")
    payment = Payment(total_amount)
    payment.process_payment(payment_method)
    print("Thank you for your purchase!")


def user_login():
    print("\nUser Login:")
    username = input("Enter username: ")

    if username in users_db:
        password = input("Enter password: ")
        user = User(username, password)
        if user.login():
            print("User login successful!")
            handle_user_flow(username)
        else:
            print("Invalid password.")
    else:
        register = input(
            "User not found. Do you want to register? (yes/no): ").strip().lower()
        if register == 'yes':
            password = input("Enter a new password: ")
            users_db[username] = password
            save_data("users",users_db)
            print("Registration successful!")
            handle_user_flow(username)
        else:
            print("Exiting...")


def main():
    print("Welcome to the Demo Marketplace!")
    user_type = input(
        "Are you an Admin or User? (Enter 'Admin' or 'User'): ").strip().lower()

    if user_type == 'admin':
        catalog = Catalog()
        admin_page(catalog)
    elif user_type == 'user':
        user_login()
    else:
        print("Invalid input. Please enter 'Admin' or 'User'.")


if __name__ == "__main__":
    main()
