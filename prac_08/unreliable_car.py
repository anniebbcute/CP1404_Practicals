from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        get_random_number = randint(0,100)
        if get_random_number < self.reliability:
            drive_car = super().drive(distance)
        else:
            distance = 0
            return distance
        return drive_car
