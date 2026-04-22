from fastapi import APIRouter, FastAPI

location_router = APIRouter()

@location_router.get('/locations')
def mock():
    return 0
