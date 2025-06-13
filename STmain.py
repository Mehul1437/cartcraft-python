import streamlit as st
import pandas as pd
from admin import Admin
from cart import Cart
from catalog import Catalog
from login import User
from payment import Payment
from utils.db_mock import users_db, save_data

catalog = Catalog()

# Initialize session state
st.session_state.setdefault("admin_logged_in", False)
st.session_state.setdefault("user_logged_in", False)
st.session_state.setdefault("cart", Cart())


def admin_page():
    st.title("Admin Dashboard")

    if not st.session_state.admin_logged_in:
        with st.form("admin_login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                admin = Admin(username, password, catalog)
                if admin.login():
                    st.session_state.admin_logged_in = True
                    st.session_state.admin = admin
                    st.success("Login successful!")
                else:
                    st.error("Invalid credentials")
        return

    action = st.selectbox("Choose action", [
                          "Add Product", "Remove Product", "View Catalog", "View Users", "Remove User"])
    if action == "Add Product":
        add_product()
    elif action == "Remove Product":
        remove_product()
    elif action == "View Catalog":
        view_catalog()
    elif action == "View Users":
        view_users()
    elif action == "Remove User":
        remove_user()


def add_product():
    st.header("Add Product")
    name = st.text_input("Product Name")
    category = st.text_input("Category")
    price = st.number_input("Price", min_value=0.01)

    if st.button("Add"):
        if name and category:
            new_product = {
                "id": len(catalog.products) + 1,
                "name": name,
                "category": category,
                "price": price
            }
            st.session_state.admin.add_product(new_product)
            st.success(f"'{name}' added successfully.")
        else:
            st.error("Please fill all fields.")


def remove_product():
    st.header("Remove Product")
    product_id = st.number_input("Product ID", min_value=1, step=1)
    if st.button("Remove"):
        st.session_state.admin.remove_product(product_id)
        st.success(f"Product with ID {product_id} removed.")


def view_catalog():
    st.header("Catalog")
    df = catalog.view_products()
    if df.empty:
        st.info("No products available.")
    else:
        st.dataframe(df)


def view_users():
    st.header("Registered Users")
    if users_db:
        st.dataframe(pd.DataFrame(users_db.items(),
                     columns=["Username", "Password"]))
    else:
        st.warning("No users found.")


def remove_user():
    st.header("Remove User")
    username = st.text_input("Username to Remove")
    if st.button("Delete User"):
        if username in users_db:
            del users_db[username]
            save_data("users",users_db)
            st.success(f"User '{username}' removed.")
        else:
            st.error("User not found.")


def user_page():
    st.title("User Dashboard")

    if not st.session_state.user_logged_in:
        with st.form("user_login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                if username in users_db and users_db[username] == password:
                    st.session_state.user_logged_in = True
                    st.session_state.user = User(username, password)
                    st.success(f"Welcome, {username}!")
                else:
                    st.error("Invalid credentials or user not found.")
                    if st.checkbox("Register as new user?"):
                        new_pass = st.text_input(
                            "New Password", type="password")
                        if st.button("Register"):
                            users_db[username] = new_pass
                            save_data("users",users_db)
                            st.success(
                                "Registered successfully. Please log in.")
        return

    view_catalog_user()


def view_catalog_user():
    st.header("Products")
    products = catalog.view_products().to_dict("records")
    if not products:
        st.warning("No products available.")
        return

    for p in products:
        st.write(f"**{p['name']}** — Rs. {p['price']} ({p['category']})")

    pid = st.number_input("Product ID", min_value=1)
    qty = st.number_input("Quantity", min_value=1)

    if st.button("Add to Cart"):
        product = next((prod for prod in products if prod["id"] == pid), None)
        if product:
            st.session_state.cart.add_to_cart(product, qty)
            st.success(f"Added {qty} x {product['name']}")
        else:
            st.error("Invalid Product ID")

    checkout()


def checkout():
    st.header("Cart Summary")
    cart_items = st.session_state.cart.view_cart()

    if not cart_items:
        st.info("Cart is empty.")
        return

    total = 0
    for item in cart_items:
        name = item["product"]["name"]
        qty = item["quantity"]
        price = item["product"]["price"]
        total += qty * price
        st.write(f"{name} x{qty} — Rs. {qty * price}")

    st.write(f"**Total: Rs. {total}**")
    method = st.selectbox("Payment Method", ["UPI", "Debit Card"])

    if st.button("Pay Now"):
        Payment(total).process_payment(method)
        st.success("Payment successful. Thank you for shopping!")


def main():
    st.set_page_config(page_title="Demo Marketplace", layout="wide")
    st.sidebar.title("Navigation")
    user_type = st.sidebar.radio("Login as:", ["Admin", "User"])

    if user_type == "Admin":
        admin_page()
    else:
        user_page()


if __name__ == "__main__":
    main()
