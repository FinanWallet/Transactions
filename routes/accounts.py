from fastapi import APIRouter, Response
from config.db import connection
from models.account import accounts
from schemas.account import Account
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

account = APIRouter()

@account.get("/accounts", response_model=list[Account], status_code=HTTP_200_OK, tags=["accounts"])
def get_accounts():
    return connection.execute(accounts.select()).fetchall()

@account.get("/accounts/{id}", tags=["accounts"])
def get_record(id: int):
    return connection.execute(accounts.select().where(account.c.id == id)).first()

@account.post("/accounts", response_model=Account, status_code=HTTP_201_CREATED, tags=["accounts"])
def create_record(account: Account):
    new_account = {"name": account.name, 
                  "limit": account.limit}
    
    result = connection.execute(accounts.insert().values(new_account))
    return connection.execute(accounts.select().where(account.c.id == result.lastrowid)).first()

@account.put("/accounts/{id}", response_model=Account, status_code=HTTP_200_OK, tags=["accounts"])
def update_record(id: int, record: Account):
    connection.execute(accounts.update().values(name=account.name, 
                                              limit=account.limit).where(account.c.id == id))
    return connection.execute(accounts.select().where(account.c.id == id)).first()

@account.delete("/accounts/{id}", status_code=HTTP_204_NO_CONTENT, tags=["accounts"])
def delete_record(id: int):
    connection.execute(accounts.delete().where(account.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)