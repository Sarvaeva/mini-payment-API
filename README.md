# Mini Payment API

Минимальный учебный сервис на **FastAPI + SQLite**.
На сегодня реализовано:
- `/health` — проверка статуса
- `/accounts` (POST) — создать аккаунт
- `/accounts/{id}` (GET) — получить аккаунт

## Запуск локально
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload