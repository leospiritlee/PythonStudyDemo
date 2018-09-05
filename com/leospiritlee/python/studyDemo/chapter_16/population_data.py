import json
from countries import get_country_code


file_name = 'population_data.json'

with open(file_name) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ':' + str(population))
        else:
            print('ERROR - ' + country_name)