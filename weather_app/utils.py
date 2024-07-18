import requests

from django.conf import settings


def get_weather_by_city(city_name: str):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    parametrs = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=parametrs)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_city_name(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    if lat and lon:
        api_key = settings.OPENWEATHERMAP_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

    return None
