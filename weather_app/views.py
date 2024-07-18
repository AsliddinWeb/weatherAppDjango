from django.shortcuts import render, redirect
from django.http import JsonResponse

# Weather
from .utils import get_weather_by_city, get_city_name


def home_page(request):
    session_city_names = request.session.get('cities', [])
    if not session_city_names:
        session_city_names = ['london']
        request.session['cities'] = session_city_names

    city_name = request.GET.get('city', session_city_names[-1])
    city_name = city_name.lower()

    ctx = {'session_city_names': session_city_names[-5:]}

    weather_data_result = get_weather_by_city(city_name)
    if weather_data_result:
        if city_name in session_city_names:
            session_city_names.remove(city_name)
        session_city_names.append(city_name)
        request.session['cities'] = session_city_names

        icon_id = weather_data_result['weather'][0]['icon']
        ctx.update({
            'icon_url': f"https://openweathermap.org/img/wn/{icon_id}@2x.png",
            'weather': weather_data_result['weather'][0]['main'],
            'weather_description': weather_data_result['weather'][0]['description'],
            'city': weather_data_result['name'],
            'country': weather_data_result['sys']['country'],
            'wind_speed': weather_data_result['wind']['speed'],
            'pressure': weather_data_result['main']['pressure'],
            'humidity': weather_data_result['main']['humidity'],
            'temperature': weather_data_result['main']['temp']
        })
    else:
        return redirect('home_page')

    return render(request, 'home.html', ctx)


def get_city_name_api(request):
    data = get_city_name(request)

    if data:
        city_name = data['name']
        return JsonResponse({'city': city_name})
    return JsonResponse({'city': None})
