import requests
from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=de58733a646de18b27f1cabf1da9417e'
    name = request.POST.get('citi')
    result = requests.get(url.format(name)).json()
    city_weather = {
        'city': name,
        'temperature': result['main']['temp'],
        'description': result['weather'][0]['description'],
        'icon': result['weather'][0]['icon'],
    }
    context = {'city_weather': city_weather}
    return render(request, "weather_app/weather.html", context)

