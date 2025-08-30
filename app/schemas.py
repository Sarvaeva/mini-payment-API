from pydantic import BaseModel, ConfigDict

class AccountBase(BaseModel):
    name: str

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    balance: float

    model_config = ConfigDict(from_attributes=True)