from fastapi import FastAPI
from routes.accounts import account
from routes.categories import category
from routes.subcategories import subcategory
from routes.records import record
from routes.payment_methods import payment_method


app = FastAPI(
    title="FinanceUN",
    description="This is a simple example of a FastAPI app with SQLAlchemy and MySQL",
    version="0.1",
    docs_url="/",
    redoc_url=None
)

routes = [record, account, category, subcategory, payment_method]

for route in routes:
    app.include_router(route)