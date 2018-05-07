def greet_user():
    print('\nhello')

greet_user()

def greet_user(name):
    print('\nHello, ' + name.title() + '!')

greet_user('jack')

greet_user('jim')

def display_message():
    print('\nI study python')

display_message()

def describe_pet(animal_type, pet_name):
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')


describe_pet('cat','tom')
describe_pet('dog','harry')

describe_pet('willie','hamster')

describe_pet(animal_type='hamster',pet_name='willie')
describe_pet(pet_name='willie',animal_type='hamster')

def describe_pet_2(pet_name, animal_type = 'dog'):
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet_2(pet_name='white')
describe_pet_2('red','cat')
describe_pet_2('green')


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return  full_name.title()

name = get_formatted_name(first_name='jack', last_name='white')
print('\n' + name)

def get_formatted_name_v2(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return  full_name.title()

name = get_formatted_name_v2(first_name='jack', middle_name='L', last_name='white')
print('\n'+ name)

def get_formatted_name_v3(first_name, last_name,middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return  full_name.title()

name = get_formatted_name_v3(first_name='jack',last_name='white')
print('\n' + name)

name = get_formatted_name_v3(first_name='jack',middle_name='l',last_name='white')
print('\n' + name)


def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person

message = build_person('jack','white')

print(message)

for key,value in message.items():
    print('\nkey: ' + key)
    print('value: '+ value.title())

print('\n')

def build_person_v2(first_name, last_name, age = ''):
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return  person
message = build_person_v2('jack','white',22)
print(message)


def greet_users(names):
    for name in names:
        print('\nHello,' + name.title() + '.')

names = ['jack','tom','harry']
greet_users(names)

print('\n')

def print_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model:' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\nThe following models have beend printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot','testA','testB']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

print(unprinted_designs)

print('\n')

def make_pizza(*toppings):
    print(toppings)

make_pizza('toppingA')
make_pizza('toppingA','toppingB','toppingC')

print('\n')

def make_pizza_v2(*toppings):
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

make_pizza_v2('toppingA')
make_pizza_v2('toppingA','toppingB','toppingC')

def make_pizza_v3(size, *toppings):
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

make_pizza_v3(12, 'toppingA')
make_pizza_v3(16, 'toppingA','toppingB','toppingC')

print('\n')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('jack','white',location='new york',field='physics')
print(user_profile)



