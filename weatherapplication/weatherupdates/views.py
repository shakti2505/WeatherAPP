from django.shortcuts import render
from .forms import WeatherForm
import requests
import json
from datetime import datetime
from .forms import WeatherForm
# Create your views here.

def index(request):
    if request.method=='POST':
        city = request.POST.get('city')
        API_KEY = 'ddeda90a9891c883d515cc2d7fc64be6'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        res = requests.get(url).json()
        print(res)
        current_time = datetime.now()
        formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
        # Weather Information
        city_weather_updates={
            'city':city,
            'temparature': 'Temperature: '+ str(res['main']['temp'])+ ' °C',
            'feelslike': 'Feels Like: ' + str(res['main']['feels_like']) + ' °C',
            'description': res['weather'][0] ['description'],
            'icon':res['weather'][0]['icon'],
            'humidity':'Humidity: ' + str(res['main']['humidity']) + '%',
            'pressure':res['main']['pressure'],
            'windspeed':str(res['wind']['speed'])+'km/h',
            'time': formatted_time
            }
    else:
        city_weather_updates={}
    return render(request, 'weatherupdates/home.html', {'weatherupdates': city_weather_updates})
