from datetime import datetime
from Database.database import Database


class Database(Database):
    def __init__(self):
        super().__init__()
        self.student = self.db["student"]

    def get_student(self, student_id):
        return self.student.find_one()
    

    def insert_student(self, data):
        return self.student.insert_one(data)
    
    # data get in few record
    def get_student_range(self, start, end):
        return self.student.find({}).skip(start).limit(end)    
    # count data
    def count_student(self):
        return self.student.count_documents({})
    
    # search data by name,number,batch,gender,premium,premium_validity,batch_code,batch_no
    def get_student_search(self, text):
        return self.student.find({
            "$or": [
                {"name": {"$regex": text, "$options": "i"}},
                # no str to int search
                {"number": {"$regex": text, "$options": "i"}},
                {"batch_code": {"$regex": text, "$options": "i"}},
                {"batch_no": {"$regex": text, "$options": "i"}},
                {"gender": {"$regex": text, "$options": "i"}},
            ]
        })
    
    # search data by name
    def get_student_search_name(self, name):
        return self.student.find({"name": {"$regex": name, "$options": "i"}})
    
    # search data by number
    def get_student_search_number(self, number):
        return self.student.find({"number": {"$regex": number, "$options": "i"}})
    
    # search data by batch
    def get_student_search_batch(self, batch):
        return self.student.find({"batch_code": {"$regex": batch, "$options": "i"}})
    
    # search data by gender
    def get_student_search_gender(self,gender):
        return self.student.find(
            {"gender": {"$regex": gender, "$options": "i"}}
        )
        
    def get_annual_payment(self,year):

        data =  self.student.find({"date": {"$gte":datetime(year, 11, 1).strftime("%d-%m-%Y"),"$lt":datetime(year+1, 10, 31).strftime("%d-%m-%Y")}})
        payment = 0
        for i in list(data):
            print(i)
            payment += i["premium"]
        return payment

    # get data order by batch code and count
    def get_student_order_by_batch_code(self):
        return self.student.aggregate([
            {
                "$group": {
                    "_id": "$batch_code",
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "_id": 1
                }
            }
        ])
    
    # get data order by batch no and count
    def get_student_order_by_batch_no(self):
        return self.student.aggregate([
            {
                "$filter":{
                
                }
            },
            
            {
                "$sort": {
                    "batch_code": 1
                }
            },
        ])