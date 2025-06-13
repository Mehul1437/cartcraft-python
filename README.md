# 🛍️ CartcraftPython – Shopping App Backend

This is a lightweight Python backend for a simple shopping app. It supports user and admin authentication, product catalog management, shopping cart functionality, and simulates a basic payment process. 😊

## Project Files 🗂️

- **[`admin.py`](https://github.com/Mehul1437/cartcraft-python/admin.py)**: Handles admin login and product management.
- **[`cart.py`](https://github.com/Mehul1437/cartcraft-python/cart.py)**: Manages the shopping cart (add, remove, view items).
- **[`catalog.py`](https://github.com/Mehul1437/cartcraft-python/catalog.py)**: View and add products to the catalog.
- **[`login.py`](https://github.com/Mehul1437/cartcraft-python/login.py)**: Validates user and admin login credentials.
- **[`main.py`](https://github.com/Mehul1437/cartcraft-python/main.py)**: The entry point of the app that connects all components.
- **[`payment.py`](https://github.com/Mehul1437/cartcraft-python/payment.py)**: Simulates the payment process.
- **[`utils/db_mock.py`](https://github.com/Mehul1437/cartcraft-python/utils/db_mock.py)**: Handles loading and saving of mock data (users, admins, products).

## Requirements ⚙️

- Python 3.x
- Libraries: `json`, `os`

Install dependencies (if any):

```bash
pip install -r requirements.txt
```

## Features 🎉

- **User Login**: Users can securely log in with their credentials.
- **Admin Login**: Admins have access to product management.
- **Product Catalog**: View and manage products in the catalog.
- **Shopping Cart**: Add, remove, and view items in the shopping cart.
- **Payment Simulation**: Mimics a simple checkout process.

## How to Start 🚀

1. Clone the repository:

   ```bash
   git clone https://github.com/Mehul1437/shop-backend.git
   cd shopping-app-backend
   ```

2. Install required dependencies.

3. Run the application:

   ```bash
   python main.py
   ```

   You're ready to log in, browse products, manage the cart, and simulate payments! 💳

## Mock Data 📂

- **Users**: Data stored in `users_data.json`.
- **Admins**: Data stored in `admins_data.json`.
- **Products**: Data stored in `products_data.json`.