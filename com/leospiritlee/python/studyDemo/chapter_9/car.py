"""一个可用于表示汽车的类"""

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return  long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def update_odometer_v2(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_card = Car('audi','a4','2016')
print(my_new_card.get_descriptive_name())
my_new_card.read_odometer()

print('\n')

my_new_card.odometer_reading = 50
my_new_card.read_odometer()

print('\n')
my_new_card.update_odometer(100)
my_new_card.read_odometer()

print('\n')
my_new_card.update_odometer_v2(80)
my_new_card.read_odometer()

print('\n')
my_new_card.update_odometer_v2(110)
my_new_card.read_odometer()


print('\n')

class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 60

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_descriptive_name(self):
        long_name = 'The car ' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_tesla = ElectricCar('tesla','model','2016')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

print('\n')

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = 300

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)


class ElectricCar_2(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery(100)

my_tesla_v2 = ElectricCar_2('teslaV2','model','2017')
print(my_tesla_v2.get_descriptive_name())
my_tesla_v2.battery.describe_battery()
my_tesla_v2.battery.get_range()





