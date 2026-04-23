from fastapi import FastAPI
from routers.forecast import forecast_router

app = FastAPI()

app.include_router(forecast_router)

