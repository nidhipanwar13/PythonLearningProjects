# demostrate polymorphism by defining a method fuel_type in both car and 
# electric car classes,but with different behaviours.

from OOPs import Car
from Inheritance import ElectricCar

class Car:
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model

    def fullname(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand + "!"

    def fuel_type(self):
        return("Petrol and Diesel") 
       
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size   

    def fuel_type(self):
        return("Electric charger")   
Tesla = ElectricCar('Tesla', 'Model S', '87KWh')
print(Tesla.fuel_type()) 
my_car = Car('Tata','Safari') 
print(my_car.fuel_type())     
    