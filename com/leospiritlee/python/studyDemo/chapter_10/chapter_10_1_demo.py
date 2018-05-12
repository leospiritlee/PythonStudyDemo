# print(5/0)
import json

try:
    answer = 5 / 0
except ZeroDivisionError:
    print('You can not divide by zero!')
else:
    print(answer)

print('\n')

def readFile(file_name):
    try:
        with open(file_name) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print('Sorry, the file' + file_name + ' does not exist.')
    else:
        print(contents)

file_name = 'testFile.txt'
readFile(file_name)

print('\n')

file_name = 'pi_digits.txt'
readFile(file_name)
print('\n')

title = 'Alice in wonderland'
titles = title.split()
print(titles)
print(len(titles))

print('\n')

def count_words(file_name):
    try:
        with open(file_name) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + file_name + ' does not exist.'
        print(msg)
    else:
        words = contents.split()
        num_wors = len(words)
        print('The file ' + file_name + 'has abount ' + str(num_wors))

file_name = 'program.txt'
count_words(file_name)

print('\n')

def count_words_v2(file_name):
    try:
        with open(file_name) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_wors = len(words)
        print('The file ' + file_name + 'has abount ' + str(num_wors))

file_name = 'programV2.txt'
count_words_v2(file_name)

print('\n')

numbers = [2,3,5,7,11,13]
print(numbers)
file_name = 'numbers.json'
with open(file_name,'w') as file_obj:
    json.dump(numbers,file_obj)

with open(file_name) as file_obj:
    numbers_v2 = json.load(file_obj)

print(numbers_v2)

print('\n')

file_name = 'username.json'
def login_user():
    try:
        with open(file_name) as file_obj:
            user_name = json.load(file_obj)
    except FileNotFoundError:
        user_name = input('What is your name?')
        with open(file_name,'w') as file_obj:
            json.dump(user_name,file_obj)
            print('We will remember you when you come back,' + user_name + '!')
    else:
        print('Welcome back, ' + user_name + '!')
login_user()



