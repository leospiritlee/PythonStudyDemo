# message = input('Tell me something, and I will repeat it back to you:')
# print(message)
#
# name = input('Please enter your name:')
# print('Hello,' + name + '!')
#
# age = input('How old are you?')
# print(age)
#
# age = int(age)
#
# if age >= 18:
#     print('you are more than 18th')


print('\n')

print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

print('\n')
# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1
#
# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += '\nEnter quit to end the program'
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     print(message)
#
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#
#
# prompt = '\nPlease enter the name of a city you have visited'
# prompt += '\nEnter quit to end the program'
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#
#     print(city)

print('\n')

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


print('\n')

unconfirmed_users = ['alice','brain','candac']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user:' + current_user.title())
    confirmed_users.append(current_user)

print(confirmed_users)

print('\n')

pets = ['dog','cat','bird','rabbit','fish']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

print('\n')

responses = {}

polling_active = True

while polling_active:

    name = input('Please enter your name')
    response = input('which book would you like to read')

    responses[name] = response

    repeat = input('Would you like to let another person respond?(y/n)')
    if repeat == 'n':
        polling_active = False


print(responses)

for name,book in responses.items():
    print(name.title() + '--' + book.title())

