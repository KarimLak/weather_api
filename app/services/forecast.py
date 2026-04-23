import json

from app.schemas.forecast import ForecastCreateDaily, ForecastCreateWeekly, ForecastResponseDaily, ForecastResponseWeekly
import openmeteo_requests
from app.core.redis import redis_client

class ForecastService:
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.openmeteo = openmeteo_requests.Client()

    def get_forecast_daily(self, payload: ForecastCreateDaily) -> ForecastResponseDaily:
        
        cache_key = f"forecast:daily:{payload.latitude}:{payload.longitude}"

        cached = redis_client.get(cache_key)
        if cached:
            return ForecastResponseDaily(**json.loads(cached))

        responses = self.openmeteo.weather_api(self.url, params = payload.model_dump())
        min_value = responses[0].Daily().Variables(0).ValuesAsNumpy().tolist()
        max_value = responses[0].Daily().Variables(1).ValuesAsNumpy().tolist()
        result = ForecastResponseDaily(
            min_temperature = min_value[0],
            max_temperature = max_value[0]
        )
        
        redis_client.setex(
                    cache_key,
                    60 * 60,  # 1 hour
                    json.dumps(result.model_dump()),
                )

        return result
    
    def get_forecast_weekly(self, payload: ForecastCreateWeekly) -> ForecastResponseWeekly:
        responses = self.openmeteo.weather_api(self.url, params = payload.model_dump())
        min_value = responses[0].Daily().Variables(0).ValuesAsNumpy().tolist()
        max_value = responses[0].Daily().Variables(1).ValuesAsNumpy().tolist()
        return ForecastResponseWeekly(
            min_temperatures = min_value,
            max_temperatures = max_value
        )
        
def get_forecast_service() -> ForecastService:
    return ForecastService()
    



