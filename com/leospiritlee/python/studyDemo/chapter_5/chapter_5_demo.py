cars = ['audi','bmw','benz','toyota']

for car in cars:

    if car is 'audi':
        print(car.title())
    else:
        print(car)

car_v1 = 'Audi'
check_flag_v1 = car_v1.lower() == 'audi'
print(check_flag_v1)

age_0 = 22
age_1 = 18
if age_0 > 21 and age_1 > 21:
    print('tes1.......')

age_1 =22
if age_0 > 21 and age_1 > 21:
    print('test2......')

requested_toppings = ['mushrooms','onions','pineapple']

if 'mushrooms' in requested_toppings:
    print('mushrooms was in requested_topping')

if 'pepperoni' not in requested_toppings:
    print('pepperoni was not in request_topping')


game_active = True
can_edit = False

car_v2 = 'subaru'

print('Is car_v2 == "subaru"? I predict True')
print(car_v2 == 'subaru')

print('\nIs car_v2 == "audi"? I predict False')
print(car_v2 == 'audi')

print('\n')

age = 19

if age > 18:
    print('You are old enough to vote!')
else:
    print('Sorry, you are too young to vote!')

print('\n')

age = 17

if age > 18:
    print('You are old enough to vote!')
else:
    print('Sorry, you are too young to vote!')

print('\n')

age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')

print('\n')

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print('Your admission cost is $' + str(price) + '.')

print('\n')
age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print('Your admission cost is $' + str(price) + '.')


print('\n')
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print('Your admission cost is $' + str(price) + '.')

print('\n')

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFinished making your pizza')
else:
    print('Are you sure you want a plain pizza?')



