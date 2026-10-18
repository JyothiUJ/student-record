# Student Record API

A FastAPI-based student management application that stores records in SQLite and supports simple AI-powered queries over the student dataset.

## Features

- Create, read, update, and delete student records
- SQLite database persistence
- Pydantic request/response schemas
- AI query endpoint using Ollama / LangChain integration
- Swagger docs via FastAPI

## Project Structure

- `main.py` - FastAPI app entry point
- `database.py` - database engine and session setup
- `models.py` - SQLAlchemy models
- `schemas.py` - request/response models
- `create_student.py` - add a student
- `get_students.py` - list all students
- `update_student.py` - update a student
- `delete_student.py` - remove a student
- `ai_query.py` - ask questions about student data
- `config.py` - app settings
- `students.db` - SQLite database file

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

4. Open the API docs:
   - http://127.0.0.1:8000/docs

## Example API Requests

### Create student
```bash
curl -X POST "http://127.0.0.1:8000/students/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","age":20,"grade":"A"}'
```

### Get students
```bash
curl "http://127.0.0.1:8000/students/"
```

### Ask a question about student data
```bash
curl -X POST "http://127.0.0.1:8000/query-students" \
  -H "Content-Type: application/json" \
  -d '{"question":"Who is the youngest student?"}'
```

## Notes

- The AI query endpoint requires an Ollama model to be available locally.
- The default model is configured in `config.py` as `llama3.2:1b`.
