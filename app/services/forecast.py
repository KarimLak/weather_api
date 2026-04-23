from app.schemas.forecast import ForecastCreateDaily, ForecastCreateWeekly
import openmeteo_requests

class ForecastService:
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.openmeteo = openmeteo_requests.Client()

    def get_forecast_daily(self, payload: ForecastCreateDaily):
        responses = self.openmeteo.weather_api(self.url, params = payload.model_dump())
        values = responses[0].Hourly().Variables(0).ValuesAsNumpy()
        return values.tolist()
    
    def get_forecast_weekly(self, payload: ForecastCreateWeekly):
        responses = self.openmeteo.weather_api(self.url, params = payload)
        return  responses[0]
        
def get_forecast_service() -> ForecastService:
    return ForecastService()
    



