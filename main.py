import json
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Database import crud, models, schemas
from Database.database import SessionLocal, engine



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/code")
def read_root(db: Session = Depends(get_db)):
    print(crud.get_user_by_date(db, "2022-01-01", "2022-12-31"))
    return {"Hello": "World"}




@app.get("/{year}/batchcode")
def read_root(year:int,db: Session = Depends(get_db)):
    start_date = f"{year-1}-12-01"
    end_date = f"{year}-11-31"
    return crud.get_user_by_batch_code_order_count(db, start_date, end_date)



@app.post("/users")
def create_user(user: schemas.StudentData, db: Session = Depends(get_db)):
    if not crud.create_user(db=db, user=user):
        raise HTTPException(status_code=400, detail="User already registered")
    return {
        "status": "success",
        "message": "User created successfully",
        "code": 200
    }

@app.get("/{year}/users", response_model=list[schemas.StudentData])
def read_users(year:int,db: Session = Depends(get_db)):
    start_date = f"{year-1}-12-01"
    end_date = f"{year}-11-31"
    users = crud.get_all_user(db, start_date, end_date)
    return users


@app.get("/premium")
def read_root(db: Session = Depends(get_db)):
    return {
        "Year": 2000,
        "Month": 1000,
    }


