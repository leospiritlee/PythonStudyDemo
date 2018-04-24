bicycles = ['trek','cann','redline','special']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

print(bicycles[1])

print(bicycles[-1])

print(bicycles[-2])

message = 'My first bicycle was a ' + bicycles[0].title()

print(message)

print('\n')

names = ['tim','lily','tom']

print(names)

print(names[0] + '-' + names[1] + '-' + names[2])

print('Hello ' + names[0].title())

print('Hello ' + names[1].title())

print('Hello ' + names[2].title())

for name in names:
    print(name)
    print(name.title()+" Morning!!!")

print('\n')

names[0] = 'jim'
print(names)

names.append('blue')

print(names)

names_2 = []

print(names_2)

names_2.append('jerry')
names_2.append('ven')
names_2.append('can')

print(names_2)

names_2.insert(0,'tom')

print(names_2)

names_2.insert(1,'mary')

print(names_2)

del names_2[1]

print(names_2)

last_name = names_2.pop()
print(last_name)

print(names_2)

names_2.remove('ven')

print(names_2)

print(len(names_2))

print('\n')


cars = ['bmw','audi','subaru']

print('Here is init list:')
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars_2 = ['bmw','audi','subaru']

print('\nHere is init list:')
print(cars_2)

print('\nHere is sorted list:')
print(sorted(cars_2))

print('\nHere is sorted reverse list:')
print(sorted(cars_2, reverse=True))

print('\nHere is init list again:')
print(cars_2)

cars_2.reverse()

print(cars_2)

cars_2.reverse()
print(cars_2)

print(len(cars_2))
