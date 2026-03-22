# ChatBotProject
FastAPI + OpenAI chatbot to convert natural language question into SQL Server SELECT query, execute it, and return conversational response.


## Features

- POST `/chat` endpoint
- GPT-4o-mini for SQL generation and response formatting
- SQL safety filter: `SELECT` only, no DML/DDL
- `pyodbc` for SQL Server
- CORS ready for frontend integration

## Files

- `main.py` - app and logic
- `config.json` - secrets / DB config

## Requirements

- Python 3.10+
- `pip install fastapi uvicorn pydantic pyodbc openai`
- ODBC Driver 17 for SQL Server

## config.json example

```json
{
  "OPENAI_API_KEY": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "DB_SERVER": "LAPTOP-CKV38OJA\\SQLEXPRESS01",
  "DB_DATABASE": "TestBotDb",
  "DB_USERNAME": "msingh",
  "DB_PASSWORD": "123456"
}
```

## Run

```bash
python -m uvicorn main:app --reload
```

## Usage

POST `http://127.0.0.1:8000/chat`

```json
{
  "user_message": "Show me total transaction amount for user 1"
}
```

Response:

```json
{
  "reply": "..."
}
```

## Notes

- `main.py` uses `user_id = 1` in `main()`.
- Keep API key private.
- If linter says `fastapi` not resolved, install `fastapi`.
- If `CORSMiddleware` unused, either use middleware or remove import.
