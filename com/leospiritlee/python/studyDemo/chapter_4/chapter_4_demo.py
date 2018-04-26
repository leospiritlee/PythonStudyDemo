peoples = ['jim','hank','blues']
for people in peoples:
    print(people)
    print(people.title() + ', hello!\n')

print('Hello everyone')
print('\n')

for value in range(1,5):
    print(value)

print('\n')

numbers = list(range(1,6))
print(numbers)

print('\n')

even_numbers = list(range(2,11,2))
print(even_numbers)

print('\n')

squares = []
for value in range(1,11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)

print(squares)
print('\n')

digits = [1,2,3,4,5,6,7,8,9,0]
min_digit = min(digits)
print(min_digit)

max_digit = max(digits)
print(max_digit)

sum_digits = sum(digits)
print(sum_digits)

print('\n')

squares_v2 = [value ** 2 for value in range(1,11)]
print(squares_v2)

print('\n')


for num in range(1,21):
    print(num)

print('\n')

squares_v3 = [num for num in range(1,1000001)]
print(len(squares_v3))
# for num in squares_v3:
#     print(num)

print('\n')

print(min(squares_v3))
print(max(squares_v3))
print(sum(squares_v3))

print('\n')

squares_v4 = [num for num in range(1,20,2)]
print(squares_v4)

print('\n')

squares_v5 = []
for num in range(3,30):
    if num % 3 == 0:
        squares_v5.append(num)
print(squares_v5)

print('\n')

##列表中 存储 1-10 的立方
squares_v6 = [num ** 3 for num in range(1,11)]
print(squares_v6)

print('\n')

##切片
players = ['jim','may','rose','jack','eli']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[4:])

print(players[-3:])

for player in players[-3:]:
    print(player.title())

print('\n')

print(max(players))
print(min(players))

print('\n')

my_foods = ['food1','food2','food3']
friend_foods = my_foods[:]

print(my_foods)

print(friend_foods)

my_foods.append('food4')

friend_foods.append('food5')

print(my_foods)

print(friend_foods)

print('\n')

my_foods_v2 = ['food1','food2','food3']
friend_foods_v2 = my_foods_v2

print(my_foods_v2)

print(friend_foods_v2)

my_foods_v2.append('food4')

friend_foods_v2.append('food5')

print(my_foods_v2)

print(friend_foods_v2)

msg = 'The first three items in the list are:'
print(msg)

print(msg[0:3])

print('\n')

dimensions = (100,150)

print(dimensions[0])

print(dimensions[1])

#'tuple' object does not support item assignment
# dimensions[0] = 250
#
# print(dimensions[0])
#
# print(dimensions[1])

print('\n')

for dimension in dimensions:
    print(dimension)

print('\n')

dimensions = (400,200)
for dimension in dimensions:
    print(dimension)

print('\n')

