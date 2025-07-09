# 🧠 FealtyX - Student API Assignment

This project is a simple REST API built with **FastAPI** that performs basic **CRUD operations** on an in-memory list of students. It also integrates with **Ollama** to generate AI-based summaries using local LLMs (e.g., LLaMA 3).

> No database used — data is stored in memory, as per assignment requirement.

---

## Features

- Create, read, update, and delete students
- Validate input using Pydantic (name, age, email)
- Detect duplicate emails
- Concurrency-safe using `asyncio.Lock`
- Validate UUID format on all ID-based routes
- AI-generated summary of a student via [Ollama](https://ollama.com/)
- Fully tested with Swagger UI, ThunderClient and curl

---

## Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- UUID
- Ollama (local LLM integration)
- asyncio for concurrency

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/manasvihow/fealtyx-assignment.git
cd fealtyx-assignment
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install and Run Ollama

> Ollama runs a local LLM (like LLaMA 3) locally on your machine.

```bash
brew install ollama  # macOS
ollama start 
ollama pull llama3
ollama run llama3
```

Leave the Ollama terminal running in the background.

---

### 5. Run the FastAPI server

```bash
uvicorn main:app --reload
```

Visit Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Example API Requests

### Create a student

```bash
curl -X POST http://localhost:8000/student/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Chris Evans", "age": 13, "email": "chris@example.com"}'
```

### Get all students

```bash
curl http://localhost:8000/student/
```

### Get a student by ID

```bash
curl http://localhost:8000/student/<uuid>
```

### Update a student

```bash
curl -X PUT http://localhost:8000/student/<uuid> \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated", "age": 22, "email": "updated@example.com"}'
```

### Delete a student

```bash
curl -X DELETE http://localhost:8000/student/<uuid>
```

### Generate AI summary for a student

```bash
curl http://localhost:8000/student/<uuid>/summary
```

---

## Notes

- This API is **in-memory only** — all data is lost when the server restarts
- Invalid UUIDs return a `422` validation error
- Concurrency is safely handled using `asyncio.Lock`
- Ollama must be running locally for summaries to work

---

## Assignment Checklist

- In-memory CRUD operations
- API endpoints tested with Swagger, ThunderClient and curl
- Ollama summary integration
- Input validation and error handling
- Concurrency handling
- Clean, modular structure
- Public repo with full instructions

---

## 📁 Project Structure

```
.
├── main.py
├── routes/
│   └── student.py
├── services/
│   └── ollama.py
├── requirements.txt
└── README.md
```

---

## 👤 Author

**Manasvi**  
[GitHub](https://github.com/manasvihow) • [Email](mailto:manasvi.bathula@gmail.com)