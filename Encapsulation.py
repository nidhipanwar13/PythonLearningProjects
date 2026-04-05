# modify the class car to encapsulate the brand attribute, making it private 
# and providing getter method to it.
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

    

    
my_result = Car('Toyota','Corolla')    
print(my_result.get_brand())    