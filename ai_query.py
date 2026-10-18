import sqlite3

from fastapi import APIRouter, HTTPException

from config import MODEL_NAME
from schemas import QueryRequest, QueryResponse

router = APIRouter(tags=["ai"])

try:
    from langchain_community.chat_models import ChatOllama

    llm = ChatOllama(model=MODEL_NAME, temperature=0)
except Exception:
    llm = None


@router.post("/query-students", response_model=QueryResponse)
def ask_student_database(payload: QueryRequest):
    if not payload.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, grade FROM students")
        rows = cursor.fetchall()
        column_names = ["id", "name", "age", "grade"]
        conn.close()

        if not rows:
            return QueryResponse(question=payload.question, answer="No student records found in the database.")

        context_data = f"Columns: {column_names}\nData Rows:\n" + "\n".join(str(row) for row in rows)
        prompt = (
            "You are a helpful assistant. Use the following database records to answer the user question.\n"
            f"Database Context:\n{context_data}\n\n"
            f"User Question: {payload.question}\n\n"
            "Answer:"
        )

        if llm is None:
            answer_text = (
                "AI model is unavailable. Please make sure Ollama is installed and the model "
                f"'{MODEL_NAME}' is pulled."
            )
        else:
            response = llm.invoke(prompt)
            answer_text = response.content if hasattr(response, "content") else str(response)

        return QueryResponse(question=payload.question, answer=answer_text)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
