# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    snowflakes = []

    def __init__(self):
        x = sd.random_number(100, 1100)
        y = sd.random_number(550, 595)
        self.snowflakes.append([x, y])
        self.color = sd.COLOR_WHITE
        self.snowflakes_length = 15

    def draw(self):
        for i in self.snowflakes:
            sd.snowflake(sd.get_point(i[0], i[1]), color=self.color, length=self.snowflakes_length)

    @staticmethod
    def clear_previous_picture():
        sd.clear_screen()

    def move(self):
        for i in self.snowflakes:
            # if i[1] < 10:
            #     sd.snowflake(sd.get_point(i[0], i[1]), color=sd.COLOR_WHITE, length=15)
            #     i[1] = 600
            #     continue
            i[1] -= 9
            i[0] += sd.random_number(-10, 10)

    def can_fall(self):
        for i in self.snowflakes:
            if i[1] < 10:
                return False
            else:
                return True


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
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
