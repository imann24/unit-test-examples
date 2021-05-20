import random


class Car:
    def __init__(self):
        self.broken = True

    def fix(self):
        self.broken = False

class CarShop:
    def __init__(self):
        self.car_colors = CarColors()

    def get_bill(self, parts_cost: int, labor_cost: int) -> int:
        return parts_cost + labor_cost

    def get_car_color(self) -> str:
        return f"Your car is {self.car_colors.get_color()}"

    def fix_car(self, car:Car):
        car.fix()

    def get_car_sell_price(self, car) -> int:
        if car.broken:
            return 1
        return 10000

class CarColors:
    def get_color(self) -> str:
        return random.choice(["red", "blue", "green"])
