from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

class ForecastCreate(BaseModel):
    latitude: float = Field(45.5017, ge=-90, le=90)
    longitude: float = Field(-73.5673, ge=-180, le=180)

class ForecastCreateDaily(ForecastCreate):
    daily: List[str] = ["temperature_2m_min", "temperature_2m_max"]
    past_days: int = 0
    forecast_days: int = 1
    timezone: str = "auto"

class ForecastCreateWeekly(ForecastCreate):
    daily: List[str] = ["temperature_2m"]
    past_days: int = 0
    forecast_days: int = 7
    timezone: str = "auto"

class ForecasteResponse(BaseModel):
# --- Location & metadata ---
    latitude: float
    longitude: float
    elevation: Optional[float] = None

    generationtime_ms: float

    timezone: str
    timezone_abbreviation: str
    utc_offset_seconds: int

    # --- Hourly ---
    hourly_units: Optional[Dict[str, str]] = None
    hourly: Optional[Dict[str, List[Union[str, float, int]]]] = None

    # --- Daily ---
    daily_units: Optional[Dict[str, str]] = None
    daily: Optional[Dict[str, List[Union[str, float, int]]]] = None



