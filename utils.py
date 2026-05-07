import requests
import constants
from config import API_KEY


def get_weather_info(city: str) -> dict:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    response = requests.get(constants.OPEN_WEATHER_API_URL, params=params)
    print(response.url)
    return {}



get_weather_info("odesa")