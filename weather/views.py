import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    cities = City.objects.all()
    API_key = 'a9f8a4972d8219a1fdd82f708dc3a6a7'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    all_cities = []
    for city_name in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'
        r = requests.get(url=url).json()

        city_info = {
            'city': city_name.name,
            'temp': r['main']['temp'],
            'icon': r['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
