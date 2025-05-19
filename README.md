# FastAPI + MongoDB Task Management API

A lightweight, modular Task Management REST API built with **FastAPI**, **MongoDB**, and **JWT-based authentication**.

---

## 🚀 Features

- Create, retrieve, and update tasks.
- Task status dropdown API.
- Pagination support for listing tasks.
- Secure endpoints using JWT (via `get_current_user`).
- Clean response formatting via custom response handler.
- MongoDB transaction handling using a decorator.

---

## 🛠️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/fastapi-mongodb-app.git
cd fastapi-mongodb-app
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn main:app --reload
```
---
## 🧪 Testing the API
- You can test the API using:
  Swagger UI or
  Postman

