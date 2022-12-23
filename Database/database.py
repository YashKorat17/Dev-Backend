import pymongo


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["devDandiya"]

    def close(self):
        self.client.close()
        
    