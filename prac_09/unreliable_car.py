""" Unreliable car class"""
from car import Car
from random import randint


class UnreliableCar(Car):
    """An unreliable version of a car."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, based on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        drive_distance = super().drive(distance)
        return drive_distance
