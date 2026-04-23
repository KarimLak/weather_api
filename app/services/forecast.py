from app.schemas.forecast import ForecasteResponse
import openmeteo_requests

class ForecastService:
    def __self__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.openmeteo = openmeteo_requests.Client()

    def get_forecast(self, payload) -> ForecasteResponse:
        responses = self.openmeteo.weather_api(self.url, params = payload)
        return responses
        
def get_forecast_service() -> ForecastService:
    return ForecastService()
    



