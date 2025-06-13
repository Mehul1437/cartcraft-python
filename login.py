from utils.db_mock import users_db, admins_db

class BaseAccount:
    def __init__(self, username, password, db, role="User"):
        self.username = username
        self.password = password
        self.db = db
        self.role = role

    def login(self):
        if self.username in self.db and self.db[self.username] == self.password:
            print(f"Welcome, {self.role} {self.username}!")
            return True
        print(f"Invalid {self.role.lower()} username or password.")
        return False


class User(BaseAccount):
    def __init__(self, username, password):
        super().__init__(username, password, users_db, role="User")


class AdminLogin(BaseAccount):
    def __init__(self, username, password):
        super().__init__(username, password, admins_db, role="Admin")
