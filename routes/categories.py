from fastapi import APIRouter, Response
from config.db import connection
from models.category import categories
from schemas.category import CategoryIn, CategoryOut
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

category = APIRouter()

@category.get("/categories", response_model=list[CategoryOut], status_code=HTTP_200_OK, tags=["categories"])
def get_categories():
    return connection.execute(categories.select()).fetchall()

@category.get("/categories/{id}", response_model=CategoryOut, tags=["categories"])
def get_category(id: int):
    return connection.execute(categories.select().where(categories.c.id == id)).first()

@category.post("/categories", response_model=CategoryIn, status_code=HTTP_201_CREATED, tags=["categories"])
def create_category(category: CategoryIn):
    new_category = {"name": category.name}
    
    result = connection.execute(categories.insert().values(new_category))
    connection.commit()  # Commit the transaction
    return connection.execute(categories.select().where(categories.c.id == result.lastrowid)).first()

@category.put("/categories/{id}", response_model=CategoryIn, status_code=HTTP_200_OK, tags=["categories"])
def update_record(id: int, category: CategoryIn):
    connection.execute(categories.update().values(name=category.name).where(categories.c.id == id))
    connection.commit()  # Commit the transaction
    return connection.execute(categories.select().where(categories.c.id == id)).first()

@category.delete("/categories/{id}", status_code=HTTP_204_NO_CONTENT, tags=["categories"])
def delete_record(id: int):
    connection.execute(categories.delete().where(categories.c.id == id))
    connection.commit()  # Commit the transaction
    return Response(status_code=HTTP_204_NO_CONTENT)