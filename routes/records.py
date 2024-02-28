from fastapi import APIRouter, Response
from config.db import connection
from models.record import records
from schemas.record import Record
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

record = APIRouter()

@record.get("/records", response_model=list[Record], status_code=HTTP_200_OK, tags=["records"])
def get_records():
    return connection.execute(records.select()).fetchall()

@record.get("/records/{id}", tags=["records"])
def get_record(id: int):
    return connection.execute(records.select().where(record.c.id == id)).first()

@record.post("/records", response_model=Record, status_code=HTTP_201_CREATED, tags=["records"])
def create_record(record: Record):
    new_record = {"date": record.date, 
                  "description": record.description, 
                  "amount": record.amount, 
                  "account": record.account_id,
                  "category_id": record.category_id, 
                  "sub_category_id": record.sub_category_id,
                  "payment_method": record.payment_method_id}
    
    result = connection.execute(records.insert().values(new_record))
    return connection.execute(records.select().where(record.c.id == result.lastrowid)).first()

@record.put("/records/{id}", response_model=Record, status_code=HTTP_200_OK, tags=["records"])
def update_record(id: int, record: Record):
    connection.execute(records.update().values(date=record.date, 
                                              description=record.description, 
                                              amount=record.amount, 
                                              account=record.account_id,
                                              category_id=record.category_id, 
                                              sub_category_id=record.sub_category_id,
                                              payment_method=record.payment_method_id).where(record.c.id == id))
    return connection.execute(records.select().where(record.c.id == id)).first()

@record.delete("/records/{id}", status_code=HTTP_204_NO_CONTENT, tags=["records"])
def delete_record(id: int):
    connection.execute(records.delete().where(record.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
