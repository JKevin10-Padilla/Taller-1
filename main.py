from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Random News API",
    description="API REST con FastAPI usando POO",
    version="1.0.0"
)

app.include_router(router)
