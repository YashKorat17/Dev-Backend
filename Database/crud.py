from sqlalchemy.orm import Session

from . import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.StudentData):
    db_user = models.Student(
        image=user.image,
        name=user.name,
        number=user.number,
        gender=user.gender,
        premium=user.premium,
        premium_validity=user.premium_validity,
        payment_type=user.payment_type,
        batch_code=user.batch_code,
        batch_no=user.batch_no,
        date=user.date,
        
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return True


# get data ordered by batch code and count of batch code
def get_user_by_batch_code_order_count(db: Session, start_date: str, end_date: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for batch_code in letters:
        count = db.query(models.Student).filter(models.Student.date.between(start_date, end_date)).filter(models.Student.batch_code == batch_code).order_by(models.Student.batch_no).count()
        if count <=200:
            if count < 10:
                return {
                    "batch_code": batch_code,
                    "batch_no": count+1,
                    "batch": f"{batch_code}0{count+1}"
                }
            else:
                return {
                    "batch_code": batch_code,
                    "batch_no": count+1,
                    "batch": f"{batch_code}{count}"
                }
        else:
            continue            



# get data between two dates
def get_user_by_date(db: Session, start_date: str, end_date: str):
    return db.query(models.Student).filter(models.Student.date.between(start_date, end_date)).all()


def get_all_user(db: Session,start_date: str, end_date: str):
    return db.query(models.Student).filter(models.Student.date.between(start_date, end_date)).order_by(models.Student.batch_code).order_by(models.Student.batch_no.asc()).all()