from django.shortcuts import render, get_object_or_404
from .models import Planet
from .utils import get_api_key
import requests

planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_sections = ['1', '2', '3']


def home(request):
    planets = Planet.objects.all()
    return render(request, 'planets_app/home.html', {'planets': planets})


def planet_detail(request, planet_name, planet_section):
    active_planet = planet_name
    active_section = planet_section

    if planet_name in planet_names and planet_section in planet_sections:
        planet = get_object_or_404(Planet, name=planet_name)
        return render(request, 'planets_app/planet_detail.html', {'planet': planet,
                                                                  'planet_names': planet_names,
                                                                  'active_planet': active_planet,
                                                                  'active_section': active_section
                                                                  })
    else:
        return render(request, 'planets_app/404.html')


def compare_planets(request):
    planet1_name = request.POST.get('planet1')
    planet2_name = request.POST.get('planet2')

    # Get data for the first planet
    planet1_data = None
    planet1_model = None
    if planet1_name:
        api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(planet1_name)
        response = requests.get(api_url, headers={'X-Api-Key': get_api_key()})
        if response.status_code == requests.codes.ok:
            json = response.json()
            if len(json) == 1:
                planet1_data = json[0]
                # only get the planet model if we managed to get the api data about the planet
                planet1_model = get_object_or_404(Planet, name=planet1_name)
        else:
            return render(request, 'planets_app/500.html')

    # Get data for the second planet
    planet2_data = None
    planet2_model = None
    if planet2_name:
        api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(planet2_name)
        response = requests.get(api_url, headers={'X-Api-Key': get_api_key()})
        if response.status_code == requests.codes.ok:
            json = response.json()
            if len(json) == 1:
                planet2_data = json[0]
                # only get the planet model if we managed to get the api data about the planet
                planet2_model = get_object_or_404(Planet, name=planet2_name)
        else:
            return render(request, 'planets_app/500.html')

    return render(request, 'planets_app/compare_planets.html', {'planet_names': planet_names,
                                                                'planet1_name': planet1_name,
                                                                'planet1_data': planet1_data,
                                                                'planet2_name': planet2_name,
                                                                'planet2_data': planet2_data,
                                                                'planet1_model': planet1_model,
                                                                'planet2_model': planet2_model,
                                                                })
