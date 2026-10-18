from fastapi import FastAPI

from ai_query import router as ai_router
from create_student import router as create_student_router
from database import init_db
from delete_student import router as delete_student_router
from get_students import router as get_students_router
from update_student import router as update_student_router

app = FastAPI(title="Student Record API")


@app.on_event("startup")
def startup_event() -> None:
    init_db()


app.include_router(get_students_router)
app.include_router(create_student_router)
app.include_router(update_student_router)
app.include_router(delete_student_router)
app.include_router(ai_router)


@app.get("/")
def root():
    return {"message": "Student Record API is running"}
