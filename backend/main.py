from fastapi import FastAPI
from routes.student import router

app = FastAPI(title="FealtyX In-Memory Student API")

app.include_router(router)
