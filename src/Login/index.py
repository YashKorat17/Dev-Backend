from fastapi import APIRouter
from .Classes.model import User,UserValidateWithMPIN
from .Classes.database import Database 
from Security.JWTauth import create_access_token

login = APIRouter(
    prefix="/api/v1/login"
)

db = Database()

@login.post("/mpin/data")
async def login_data(user: UserValidateWithMPIN):
    data = db.get_user(user.mpin)
    if not data:
        return {"message": "Login data not found"}
    
    return {
        "Status": "Success",
        "Message": "Login data found",
        "access_token": create_access_token({"username": data["username"]}),
        "token_type": "bearer"
    }

@login.post("/create")
async def login_create(user: User):
    user = user.dict()
    db.create_user(user)
    return {"message": "Login create"}