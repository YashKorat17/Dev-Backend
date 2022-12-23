from Database.database import Database
from Security.JWTauth import get_password_hash

class Database(Database):
    def __init__(self):
        super().__init__()
        self.user = self.db["user"]

    def get_user(self, mpin):
        return self.user.find_one({"mpin": mpin})

    def create_user(self, data):
        data["password"] = get_password_hash(data["password"])        
        return self.user.insert_one(data)