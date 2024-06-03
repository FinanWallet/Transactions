from fastapi import APIRouter, Response
from config.db import connection
from models.record import records
from schemas.record import RecordIn, RecordOut, RecordUpdate
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

record = APIRouter()

@record.get("/records/{user_id}", response_model=list[RecordOut], status_code=HTTP_200_OK, tags=["records"])
def get_records(user_id: int):
    print(user_id)
    return connection.execute(records.select().where(records.c.user_id == user_id)).fetchall()

@record.get("/records/{user_id}/{id}", response_model=RecordOut, tags=["records"])
def get_record(id: int, user_id: int):
    print(id,user_id)
    return connection.execute(records.select().where((records.c.id == id) & (records.c.user_id == user_id))).first()

@record.post("/records", response_model=RecordOut, status_code=HTTP_201_CREATED, tags=["records"])
def create_record(record: RecordIn):
    new_record = {"user_id": record.user_id,
                  "account_id": record.account_id,
                  "category_id": record.category_id,
                  "subcategory_id": record.subcategory_id,
                  "type": record.type,
                  "date": record.date, 
                  "amount": record.amount, 
                  "description": record.description}
    
    result = connection.execute(records.insert().values(new_record))
    connection.commit()  # Commit the transaction
    return connection.execute(records.select().where(records.c.id == result.lastrowid)).first()

@record.put("/records/{id}", response_model=RecordOut, status_code=HTTP_200_OK, tags=["records"])
def update_record(id: int, record: RecordUpdate):
    connection.execute(records.update().values(account_id=record.account_id,
                                               category_id=record.category_id,
                                               subcategory_id=record.subcategory_id,
                                               type=record.type,
                                               date=record.date, 
                                               amount=record.amount, 
                                               description=record.description).where(records.c.id == id))
    
    connection.commit()  # Commit the transaction
    return connection.execute(records.select().where(records.c.id == id)).first()

@record.delete("/records/{id}", status_code=HTTP_204_NO_CONTENT, tags=["records"])
def delete_record(id: int):
    connection.execute(records.delete().where(records.c.id == id))
    connection.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# @record.get("/records/{user_id}", response_model=RecordOut, tags=["records"])
# def delete_record_by_user(user_id: int):
#     connection.execute(records.delete().where(records.c.user_id == user_id))
#     connection.commit()
#     return Response(status_code=HTTP_204_NO_CONTENT)
