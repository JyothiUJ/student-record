from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import StudentCreate, StudentRead

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/", response_model=StudentRead, status_code=201)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(Student).filter(Student.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Student with this name already exists")

    student = Student(name=payload.name, age=payload.age, grade=payload.grade)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
