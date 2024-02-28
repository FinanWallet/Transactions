from fastapi import APIRouter, Response
from config.db import connection
from models.payment_method import payment_methods
from schemas.payment_method import Payment_method
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

payment_method = APIRouter()

@payment_method.get("/payment_methods", response_model=list[Payment_method], status_code=HTTP_200_OK, tags=["payment_methods"])
def get_payment_methods():
    return connection.execute(payment_methods.select()).fetchall()

@payment_method.get("/payment_methods/{id}", tags=["payment_methods"])
def get_payment_method(id: int):
    return connection.execute(payment_methods.select().where(payment_method.c.id == id)).first()

@payment_method.post("/payment_methods", response_model=Payment_method, status_code=HTTP_201_CREATED, tags=["payment_methods"])
def create_payment_method(payment_method: Payment_method):
    new_payment_method = {"name": payment_method.name}
    
    result = connection.execute(payment_methods.insert().values(new_payment_method))
    return connection.execute(payment_methods.select().where(payment_method.c.id == result.lastrowid)).first()

@payment_method.put("/payment_methods/{id}", response_model=Payment_method, status_code=HTTP_200_OK, tags=["payment_methods"])
def update_payment_method(id: int, payment_method: Payment_method):
    connection.execute(payment_methods.update().values(name=payment_method.name).where(payment_method.c.id == id))
    return connection.execute(payment_methods.select().where(payment_method.c.id == id)).first()

@payment_method.delete("/payment_methods/{id}", status_code=HTTP_204_NO_CONTENT, tags=["payment_methods"])
def delete_payment_method(id: int):
    connection.execute(payment_methods.delete().where(payment_method.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)