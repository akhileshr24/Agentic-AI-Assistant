import os
import json
import requests
from langchain_core.tools import tool

@tool
def get_weather_data(city: str) ->dict:
    """Get the current weather information for a city using this."""

    api_key = os.getenv("WEATHERSTACK_API_KEY")

    url = "https://api.weatherstack.com/current"

    params = {
        "access_key": api_key,
        "query":city,
        "units": "m"     

    }

    response=requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()
    # print(json.dumps(data,indent=4))

     # Weatherstack can return API errors inside JSON.
    if "error" in data:
        raise ValueError(data["error"]["info"])

    current = data["current"]
    location = data["location"]

    return {
        "city": location["name"],
        "country": location["country"],
        "temperature": current["temperature"],
        "weather": current["weather_descriptions"][0],
        "humidity": current["humidity"],
        "wind_speed": current["wind_speed"],
    }
