from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def create_account(db: Session, data: schemas.AccountCreate):
    acc = models.Account(name=data.name, balance=data.balance)
    db.add(acc)
    db.commit()
    db.refresh(acc)
    return acc

def get_account(db: Session, account_id: int):
    acc = db.query(models.Account).filter(models.Account.id == account_id).first()
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc