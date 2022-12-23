from fastapi import APIRouter, Depends

from .Classes.database import Database
from .Classes.model import SearchBatch, SearchGender, SearchName, SearchNumber, SearchPremium, SearchText, StudentData


studentdata = APIRouter(
    prefix="/api/v1/studentdata"
)
async def get_db():
    db = Database()
    try :
        yield db
    finally:
        db.close()


@studentdata.get("/count")
async def studentdata_count(db: Database = Depends(get_db)):
    count = db.count_student()
    return {
            "no": count,
            "start": 0,
            "end": count-1
        }



@studentdata.get("/{start}/{end}",response_model=list[StudentData])
async def studentdata_get(start:int, end:int, db: Database =Depends(get_db)):
    return list(db.get_student_range(start, end))




@studentdata.post("/")
async def studentdata_post(data: StudentData, db: Database = Depends(get_db)):
    db.insert_student(data.dict())
    return {
        "status": "success",
        "message": "data inserted"
    }
 

@studentdata.get("/search",response_model=list[StudentData])
async def studentdata_search(text:SearchText, db: Database = Depends(get_db)):
    # TODO:NUMBER NOT WORKING
    return list(db.get_student_search(text.text))


@studentdata.get("/search/number",response_model=list[StudentData])
async def studentdata_search_number(number:SearchNumber, db: Database = Depends(get_db)):
    return list(db.get_student_search_number(number))

@studentdata.get("/search/name",response_model=list[StudentData])
async def studentdata_search_name(name:SearchName, db: Database = Depends(get_db)):
    return list(db.get_student_search_name(name))

@studentdata.get("/search/batch",response_model=list[StudentData])
async def studentdata_search_batch(batch:SearchBatch, db: Database = Depends(get_db)):
    return list(db.get_student_search_batch(batch))

@studentdata.get("/gender",response_model=list[StudentData])
async def studentdata_search_gender(batch:SearchGender, db: Database = Depends(get_db)):
    return list(db.get_student_search_gender(batch))

@studentdata.get("/annual_payment")
async def studentdata_annual_payment(year:SearchPremium, db: Database = Depends(get_db)):
    return {
        "payment": db.get_annual_payment(year.year)
    }

@studentdata.get("/batch")
async def studentdata_batch(db: Database = Depends(get_db)):
    # return list(db.get_student_order_by_batch_code_A())
    return db.get_student_order_by_batch_code_A()