# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(10, 500)
        self.y = sd.random_number(500, 600)
        self.color = sd.COLOR_WHITE
        self.snowflakes_length = 15

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.snowflakes_length, color=self.color)

    def move(self):
        self.y -= 20
        self.x += sd.random_number(-10, 10)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.snowflakes_length, color=sd.background_color)

    def can_fall(self):
        return self.y > 30


flake = Snowflake()


def get_flakes(count):
    snowflake_list = []
    for _ in range(count):
        snowflake_list.append(Snowflake())
    return snowflake_list


def get_fallen_flakes():
    fallen_num = 0
    for _ in flakes:
        if not flake.can_fall():
            fallen_num += 1
    return fallen_num


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())


flakes = get_flakes(count=1)
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
# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
