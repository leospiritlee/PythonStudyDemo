class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


myDog = Dog('jerry',3)
print("My dog's name is " + myDog.name.title() + '.')
print('My dog is ' + str(myDog.age) + ' years old.')
myDog.sit()
myDog.roll_over()

print('\n')

yourDog = Dog('tom',4)
print("Your dog's name is " + yourDog.name.title() + '.')
print('Your dog is ' + str(yourDog.age) + ' years old.')
yourDog.sit()
yourDog.roll_over()

