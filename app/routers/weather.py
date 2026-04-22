from fastapi import APIRouter, FastAPI

weather_router = APIRouter()

@weather_router.get('/weather')
def mock():
    return 0

@weather_router.get('/weather/{location}')
def mock():
    return 0






