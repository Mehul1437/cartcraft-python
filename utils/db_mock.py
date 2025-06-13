import json
import os

DATA_FILES = {
    "users": ("users_data.json", dict),
    "admins": ("admins_data.json", dict),
    "products": ("products_data.json", list),
}


def load_data(file_key):
    file_path, default_type = DATA_FILES[file_key]
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return default_type()


def save_data(file_key, data):
    file_path, _ = DATA_FILES[file_key]
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# Example usage
users_db = load_data("users")
admins_db = load_data("admins")
products_db = load_data("products")