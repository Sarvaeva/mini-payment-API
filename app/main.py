from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import db, models, schemas, crud
from contextlib import asynccontextmanager
from .db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup")
    init_db()
    yield
    print("Shutdown")


app = FastAPI(title="Mini Payment API", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/accounts", response_model=schemas.Account)
def create_account(payload: schemas.AccountCreate, session: Session = Depends(db.get_db)):
    return crud.create_account(session, payload)


@app.get("/accounts/{account_id}", response_model=schemas.Account)
def read_account(account_id: int, session: Session = Depends(db.get_db)):
    return crud.get_account(session, account_id)