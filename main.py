from fastapi import FastAPI
from src.Login.index import login
from src.StudentData.index import studentdata

app = FastAPI()


app.include_router(login)
app.include_router(studentdata)

