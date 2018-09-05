import json
import pygal.maps.world
from countries import get_country_code

file_name = 'population_data.json'
with open(file_name) as f:
    result_data = json.load(f)

cc_populations = {}

for pop_dict in result_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)
wm.render_to_file('world_population.svg')






