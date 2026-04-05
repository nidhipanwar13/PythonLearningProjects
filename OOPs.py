# class and object
# create a class car with attributes like brand and  model. Then create an instance of this class.

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_Tesla = ElectricCar('Tesla', 'Model S', '87KWh')
print(my_Tesla.battery_size)
print(my_Tesla.fullname())

my_car = Car('Toyota','Corolla')  
my_new_car = Car('Tata','Safari') 
print(my_car.fullname())     
print(my_car.brand)
print(my_car.model)
print(my_new_car.model)

# Inheritance
# create an electric car class that inherists from the car class and has an additional attribute battery_size.

