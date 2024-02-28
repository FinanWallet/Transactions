from fastapi import APIRouter, Response
from config.db import connection
from models.subcategory import subcategories
from schemas.subcategory import Subcategory
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

subcategory = APIRouter()

@subcategory.get("/subcategories", response_model=list[Subcategory], status_code=HTTP_200_OK, tags=["subcategories"])
def get_subcategories():
    return connection.execute(subcategories.select()).fetchall()

@subcategory.get("/subcategories/{id}", tags=["subcategories"])
def get_subcategory(id: int):
    return connection.execute(subcategories.select().where(subcategory.c.id == id)).first()

@subcategory.post("/subcategories", response_model=Subcategory, status_code=HTTP_201_CREATED, tags=["subcategories"])
def create_subcategory(subcategory: Subcategory):
    new_subcategory = {"name": subcategory.name,
                  "account": subcategory.account,
                  "category": subcategory.category}
    
    result = connection.execute(subcategories.insert().values(new_subcategory))
    return connection.execute(subcategories.select().where(subcategory.c.id == result.lastrowid)).first()

@subcategory.put("/subcategories/{id}", response_model=Subcategory, status_code=HTTP_200_OK, tags=["subcategories"])
def update_subcategory(id: int, subcategory: Subcategory):
    connection.execute(subcategories.update().values(name=subcategory.name, 
                                              account=subcategory.account,
                                              category=subcategory.category).where(subcategory.c.id == id))
    return connection.execute(subcategories.select().where(subcategory.c.id == id)).first()

@subcategory.delete("/subcategories/{id}", status_code=HTTP_204_NO_CONTENT, tags=["subcategories"])
def delete_subcategory(id: int):
    connection.execute(subcategories.delete().where(subcategory.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)