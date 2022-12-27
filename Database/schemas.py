from pydantic import BaseModel, Field
from datetime import date, datetime

class StudentData(BaseModel):    
    image : bytes = b"" 
    name : str
    number:int
    gender : str
    premium:float
    premium_validity:str
    payment_type:str
    batch_code:str
    batch_no:int 
    date: date
    
    class Config:
        orm_mode = True


# {
#   "image":"",
#   "name": "lalan",
#   "number":  "8154012738",
#   "gender": "Male",
#   "premium": 2000,
#   "premium_validity": "Year",
#   "payment_type": "Online",
#   "batch_code": "C",
#   "batch_no": 1,
#   "date": "2022-12-27"
# }


