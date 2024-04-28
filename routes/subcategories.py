from fastapi import APIRouter, Response
from config.db import connection
from models.subcategory import subcategories
from schemas.subcategory import SubcategoryIn, SubcategoryOut
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

subcategory = APIRouter()

@subcategory.get("/subcategories", response_model=list[SubcategoryOut], status_code=HTTP_200_OK, tags=["subcategories"])
def get_subcategories():
    return connection.execute(subcategories.select()).fetchall()

@subcategory.get("/subcategories/{id}", response_model=SubcategoryOut, tags=["subcategories"])
def get_subcategory(id: int):
    return connection.execute(subcategories.select().where(subcategories.c.id == id)).first()

@subcategory.post("/subcategories", response_model=SubcategoryIn, status_code=HTTP_201_CREATED, tags=["subcategories"])
def create_subcategory(subcategory: SubcategoryIn):
    new_subcategory = {"name": subcategory.name,
                       "category_id": subcategory.category_id}
    
    result = connection.execute(subcategories.insert().values(new_subcategory))
    connection.commit() # Commit the transaction
    return connection.execute(subcategories.select().where(subcategories.c.id == result.lastrowid)).first()

@subcategory.put("/subcategories/{id}", response_model=SubcategoryIn, status_code=HTTP_200_OK, tags=["subcategories"])
def update_subcategory(id: int, subcategory: SubcategoryIn):
    connection.execute(subcategories.update().values(name=subcategory.name, 
                                              category_id=subcategory.category_id).where(subcategories.c.id == id))
    
    connection.commit()  # Commit the transaction
    return connection.execute(subcategories.select().where(subcategories.c.id == id)).first()

@subcategory.delete("/subcategories/{id}", status_code=HTTP_204_NO_CONTENT, tags=["subcategories"])
def delete_subcategory(id: int):
    connection.execute(subcategories.delete().where(subcategories.c.id == id))
    connection.commit() # Commit the transaction
    return Response(status_code=HTTP_204_NO_CONTENT)