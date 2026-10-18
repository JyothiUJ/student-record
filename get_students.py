from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import StudentRead

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=list[StudentRead])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
