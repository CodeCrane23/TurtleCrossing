import random
from turtle import Turtle


class CarManager:
    def __init__(self):
        self.all_cars=[]

    def create_car(self):
        random_chance= random.randint(1,6)
        if random_chance == 1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            r = random.randint(25, 255)
            g = random.randint(25, 255)
            b = random.randint(25, 255)
            new_car.color(r, g, b)
            i = random.randrange(-240, 240)
            new_car.goto(300, i)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)




