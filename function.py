import json
import math

def read_file(input_val):
    with open(input_val, 'r') as openfile:
        # Reading from json file
        return json.load(openfile)


do_it = lambda f: f + 1
output = list(map(do_it, [1,2,3]))


# example of a method
class Car(object):
    def __init__(self):
        self._speed = 100

    @property
    def speed(self):
        print("speed is", self._speed)
        return self._speed

    @speed.setter
    def speed(self, value):
        print("Setting to", value)
        self._speed = value


# example of static method
class RightTriangle(object):
    @staticmethod
    def hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)

    @staticmethod
    def sin(a, b):
        return a / RightTriangle.hypotenuse(a, b)

    @staticmethod
    def cos(a, b):
        return b / RightTriangle.hypotenuse(a, b)


if __name__ == "__main__":
    car = Car()
    car.speed = 80
    x = car.speed

    print(RightTriangle.hypotenuse(3, 4))
    rt = RightTriangle()

    print(rt.sin(3,4))
