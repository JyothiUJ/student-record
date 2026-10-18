from typing import Optional

from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):
    name: str
    age: int
    grade: str


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[str] = None


class StudentRead(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str
