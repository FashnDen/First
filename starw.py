import requests

url = 'https://swapi.dev/api/'

response = requests.get(url)

response = response.json()

planetsApi = response['planets']

responsePlanet = requests.get(planetsApi).json()
print(responsePlanet)
def check_planets(url):
    planets = []
    diameters = []
    planets_dict = {}
    for i in range(1, 11):
        response = requests.get(url + '/' + str(i)).json()
        planets.append(response['name'])
        diameters.append(int(response['diameter']))
        # print('Планета', response['name'], 'имеет диаметр', response['diameter'], 'условных единиц')
        planets_dict = {diameters[x]: planets[x] for x in range(len(planets))}
    print('Планета', planets_dict[max(diameters)], 'имеет наибольший диаметр -', max(diameters))

check_planets(planetsApi)
print(responsePlanet['diameter'])
def largest(url):
    global check_planets
    return responsePlanet[planets_dict[max(diameters)]]


