from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field

class ForecastCreate(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    hourly: str = Field(...)
    past_days: int = Field(..., ge=0)
    forecast_days: int = Field(..., ge=0)

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

