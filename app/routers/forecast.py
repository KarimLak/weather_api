from fastapi import APIRouter, FastAPI

forecast_router = APIRouter()

@forecast_router.get('/forecast')
def mock():
    return 0

@forecast_router.get('/forecast/daily/{location}')
def mock():
    return 0

@forecast_router.get('/forecast/weekly/{location}')
def mock():
    return 0







