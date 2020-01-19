# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, 600)
        self.y = sd.random_number(450, 570)
        self.name = 'Снежинка'
        self.length = 20

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE)

    def move(self):
        self.y -= 20
        self.x += sd.random_number(-10, 10)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def can_fall(self):
        return self.y > 20


flake = Snowflake()


def get_flakes(count):
    lists_snowflake = []
    for _ in range(count):
        lists_snowflake.append(Snowflake())
    return lists_snowflake


def get_fallen_flakes():
    numbers = 0
    for _ in flakes:
        if not flake.can_fall():
            numbers += 1
    return numbers


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())


flakes = get_flakes(count=5)
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()
    if fallen_flakes:
        append_flakes(count=fallen_flakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
