from abc import ABC, abstractmethod
from typing import Self

class Transport(ABC):
    def __init__(self, fuel: int, condition: float | int):
        self.fuel = fuel
        self.condition = condition

    @property
    def is_working(self) -> bool:
        return self.condition > 20

    @abstractmethod
    def __str__(self) -> str:
        return ''

    def move(self, distance: int | float):
        if not self.is_working:
            print('Transport is broken')
            return
        fuel_needed = distance

        if self.fuel < fuel_needed:
            print('Not enough fuel')
            return

        self.fuel -= fuel_needed
        self.condition -= distance * 0.1
        print(f'Transport moved {distance} km')

class Car(Transport):

    def __init__(self, model: str):
        super().__init__(fuel=50, condition=100)
        self.model = model

    def __str__(self):
        return f'Car {self.model} | fuel = {self.fuel} | condition = {self.condition}'

class Truck(Transport):

    def __init__(self, name: str):
        super().__init__(fuel=120, condition=100)
        self.name = name

    def __str__(self):
        return f'Truck {self.name} | fuel = {self.fuel} | condition = {self.condition}'

class Motorcycle(Transport):

    def __init__(self, brand: str,):
        super().__init__(fuel=20, condition=100)
        self.brand = brand

    def __str__(self):
        return f'Motorcycle {self.brand} | fuel = {self.fuel} | condition = {self.condition}'

car = Car("BMW")
truck = Truck("Volvo")
motorcycle = Motorcycle("Yamaha")

print(car)
car.move(10)
print(car)
car.move(100)

print(car.is_working)
print(car.__dict__)
motorcycle.move(100)

truck.condition = 10
truck.move(5)

class ServiceStation():

    def repair(self, transport_unit: Transport):

        if transport_unit.condition >= 20:
            print('Transport is already fully repaired')
            return

        transport_unit.condition = min(
            100,
            transport_unit.condition + 20
        )

        print('Transport repaired')

service = ServiceStation()

car.move(99)
print(car)
service.repair(car)
print(car)

truck.condition = 0
print(truck)
service.repair(truck)
print(truck)


motorcycle.condition = 50

print(motorcycle)

service.repair(motorcycle)
service.repair(motorcycle)
service.repair(motorcycle)

print(motorcycle)