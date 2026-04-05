# create an electric car class that inherists from the car class and has an additional attribute battery_size.

# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model

#     def fullname(self):
#         return f"{self.brand} {self.model}"

from OOPs import Car

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_Tesla = ElectricCar('Tesla', 'Model S', '87KWh')
print(my_Tesla.battery_size)
print(my_Tesla.fullname())
