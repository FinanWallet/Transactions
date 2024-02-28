from fastapi import APIRouter, Response
from config.db import connection
from models.category import categories
from schemas.category import Category
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

category = APIRouter()

@category.get("/categories", response_model=list[Category], status_code=HTTP_200_OK, tags=["categories"])
def get_categories():
    return connection.execute(categories.select()).fetchall()

@category.get("/categories/{id}", tags=["categories"])
def get_category(id: int):
    return connection.execute(categories.select().where(category.c.id == id)).first()

@category.post("/categories", response_model=Category, status_code=HTTP_201_CREATED, tags=["categories"])
def create_category(category: Category):
    new_category = {"name": category.name, 
                  "account": category.account,
                  "limit": category.limit}
    
    result = connection.execute(categories.insert().values(new_category))
    return connection.execute(categories.select().where(category.c.id == result.lastrowid)).first()

@category.put("/categories/{id}", response_model=Category, status_code=HTTP_200_OK, tags=["categories"])
def update_record(id: int, category: Category):
    connection.execute(categories.update().values(name=category.name, 
                                              account=category.account_id,
                                              limit=category.limit).where(category.c.id == id))
    return connection.execute(categories.select().where(category.c.id == id)).first()

@category.delete("/categories/{id}", status_code=HTTP_204_NO_CONTENT, tags=["categories"])
def delete_record(id: int):
    connection.execute(categories.delete().where(category.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)