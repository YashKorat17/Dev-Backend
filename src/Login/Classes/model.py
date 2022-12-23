from datetime import datetime
from pydantic import UUID4, BaseModel, Field






class User(BaseModel):
    username:str
    password : str
    group : str
    mpin: int 

    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class UserValidateWithMPIN(BaseModel):
    mpin: int 
