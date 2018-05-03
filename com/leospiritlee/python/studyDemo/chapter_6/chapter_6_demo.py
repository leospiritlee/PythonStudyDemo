alien_0 = {'color':'green', 'points': 5}

print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

print('\n')

new_points = alien_0['points']

print('You just earned ' + str(new_points) + ' points!')

print('\n')

alien_0['x_position'] = 0
print(alien_0)

alien_0['y_position'] =25
print(alien_0)

print('\n')

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)

print('The alien_1 is ' + alien_1['color'] + '.')

alien_1['color'] = 'yellow'
print('The alien_1 now is ' + alien_1['color'] + '.')

alien_2 = {'x_position':0, 'y_position':25,'speed':'medium'}
print(alien_2)
if alien_2['speed'] is 'slow':
    x_increment = 1
elif alien_2['speed'] is 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment

print(alien_2)

del alien_2['speed']
print(alien_2)

print('\n')

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

print(favorite_languages)
print("Sarah's favorite_languages is " + favorite_languages['sarah'].title() + '.')

for key, value in favorite_languages.items():
    print('\nkey:' + key)
    print('value:' + value)
    print(key.title() + "'s favorite_languages is  " + value.title())

print('\n')

for name in favorite_languages.keys():
    print('\n'+name)
    print(favorite_languages[name])

print('\n')

for value in favorite_languages.values():
    print(value)

print('\n')

friends = ['phli','edward']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print('hi, ' + name.title() + ', I see your favourite_language is ' + favorite_languages[name].title() + '.')

print('\n')

for name in sorted(favorite_languages.keys()):
    print(name.title())

print('\n')

for value in set(favorite_languages.values()):
    print(value)

print('\n')

aliens = [alien_0,alien_1,alien_2]
print(aliens)

for alien in aliens:
    print(alien)

print('\n')

aliens = []
for alien_num in range(30):
    new_alien = {'color':'red','points':15,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(len(aliens))

for alien in aliens[0:3]:
    alien['color'] = 'greed'
    alien['points'] = 5
    alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)

print('\n')

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}

print(pizza)

print(pizza['crust'])
print(pizza['toppings'])
print(pizza['toppings'][0])
print(pizza['toppings'][1])

for topping in pizza['toppings']:
    print(topping)

print('\n')

favorite_languages = {

    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite_language are :")
    for language in languages:
        print('\t' + language.title())

print('\n')

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }

}

print(users)

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first']+ ' ' + user_info['last']
    location = user_info['location']

    print('\tFullname: ' + full_name.title())
    print('\tLocation: ' + location.title())