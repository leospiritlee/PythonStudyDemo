with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('\n')

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n')

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print('\n')

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


file_name = 'program.txt'
with open(file_name,'w') as file_object:
    file_object.write('I love python\n')
    file_object.write('I love creating new games\n')

with open(file_name,'a') as file_object:
    file_object.write('I also love Java\n')
    file_object.write('I love creating web\n')







