from datetime import datetime
from pydantic import BaseModel, Field

from Common.random import random_str_generator


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
    date: str = Field(default_factory=lambda: datetime.now().strftime("%d-%m-%Y")) 

    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class SearchText(BaseModel):
    text:str

class SearchName(BaseModel):
    name:str

class SearchNumber(BaseModel):
    number:int

class SearchBatch(BaseModel):
    batch:str   

class SearchGender(BaseModel):
    gender:str

class SearchPremium(BaseModel):
    year:int