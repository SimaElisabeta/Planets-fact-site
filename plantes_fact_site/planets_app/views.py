from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Planet, AtmosphericComposition
import requests

# UTILS
planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_sections = ['1', '2', '3']


# create data about a planet in the form of a dict which will be included in a JSON response
def create_planet_dict(planet_name):
    planet = Planet.objects.get(name=planet_name)
    planet_atmospheric_compositions = AtmosphericComposition.objects.filter(planet=planet.id)
    substances = [composition.substance.get_substance_display() for composition in planet_atmospheric_compositions]
    percentages = [composition.percent for composition in planet_atmospheric_compositions]

    atmosphere = []

    for i in range(0, len(substances)):
        element = {'substance': substances[i], 'percent': percentages[i]}
        atmosphere.append(element)

    response = {'name': planet.name,
                'mass': planet.mass,
                'gravity': planet.gravity,
                'distance_sun': planet.distance_sun,
                'moons_num': planet.moons_num,
                'rings': planet.rings,
                'category_id': planet.category_id.planet_category,
                'rotation': planet.rotation,
                'revolution': planet.revolution,
                'radius': planet.radius,
                'temperature': planet.temperature,
                'atmosphere': atmosphere
                }
    return response


# creates a JSON response for error cases
def create_error_json(message):
    message_dict = {'message': message
                    }
    return JsonResponse(message_dict, safe=False, json_dumps_params={'indent': 1}, status=400)


# used to validate variables received in a GET request
def validate_api_data(request, valid_var_names):
    if request.method != 'GET':
        return create_error_json(f'Invalid request method: {request.method}. Expected GET.')

    get_data_request = request.GET.dict()
    invalid_var_names = []
    empty_var_names = []

    for key, value in get_data_request.items():
        if key not in valid_var_names:
            invalid_var_names.append(key)
        else:
            if value is None or len(value) == 0:
                empty_var_names.append(key)

    if len(invalid_var_names) > 0:
        separator = ', '
        return create_error_json('Invalid variable names: {}'.format(separator.join(invalid_var_names)))

    if len(empty_var_names) > 0:
        separator = ', '
        return create_error_json('No value specified for variables: {}'.format(separator.join(empty_var_names)))
    return None


# VIEW functions
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

    planet1_data = None
    planet2_data = None
    planet1_model = None
    planet2_model = None

    if planet1_name and planet2_name:
        # Get the root URL of the site
        root_url = request.build_absolute_uri('/')
        if not root_url.endswith('/'):
            root_url += '/'

        # Use own API to get data about the compared planets
        api_url = f'{root_url}api/v1/planets/?planet1={planet1_name}&planet2={planet2_name}'
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            json = response.json()
            if len(json) == 2:
                planet1_data = json[0]
                planet2_data = json[1]

                # only get the planet model if we managed to get the api data about the planet
                planet1_model = get_object_or_404(Planet, name=planet1_name)
                planet2_model = get_object_or_404(Planet, name=planet2_name)
            else:
                return render(request, 'planets_app/500.html')
        else:
            return render(request, 'planets_app/500.html')

    return render(request, 'planets_app/compare_planets.html', {'planet_names': planet_names,
                                                                'planet1_name': planet1_name,
                                                                'planet2_name': planet2_name,
                                                                'planet1_data': planet1_data,
                                                                'planet2_data': planet2_data,
                                                                'planet1_model': planet1_model,
                                                                'planet2_model': planet2_model,
                                                                })


def api_planet(request):
    valid_var_names = ['planet1', 'planet2']
    error_json = validate_api_data(request, valid_var_names)

    # return error message if requested var names are not valid
    if error_json is not None:
        return error_json

    planet1_requested = request.GET.get('planet1', None)
    planet2_requested = request.GET.get('planet2', None)

    # return error message if request contains only variable name planet2
    if planet2_requested is not None and planet1_requested is None:
        return create_error_json('planet2 can only be used if planet1 is also specified')

    # get all planets data
    planets = Planet.objects.all()

    planets_data = []

    # get data for planet1 and planet2
    if planet1_requested is not None and planet1_requested in planet_names:
        planet1_dict = create_planet_dict(planet1_requested)
        planets_data.append(planet1_dict)
        if planet2_requested is not None and planet2_requested in planet_names:
            planet2_dict = create_planet_dict(planet2_requested)
            planets_data.append(planet2_dict)

    # get data for all planets
    if planet1_requested is None and planet2_requested is None:
        for planet in planets:
            planet_dict = create_planet_dict(planet.name)
            planets_data.append(planet_dict)

    return JsonResponse(planets_data, safe=False, json_dumps_params={'indent': 1})


# api help page under construction
def api_help(request):
    return render(request, 'planets_app/api_help.html')
