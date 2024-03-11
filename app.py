from fastapi import FastAPI
from routes.categories import category
from routes.subcategories import subcategory
from routes.records import record


app = FastAPI(
    title="FinanceUN",
    description="This is a simple example of a FastAPI app with SQLAlchemy and MySQL",
    version="0.1",
    docs_url="/",
    redoc_url=None
)

routes = [record, category, subcategory]

for route in routes:
    app.include_router(route)