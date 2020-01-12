# -*- coding: utf-8 -*-
from random import randint

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
import simple_draw as sd

snowflake = []


def create(n):
    for _ in range(n):
        x = sd.random_number(0, 500)
        y = sd.random_number(100, 700)
        snowflake.append([x, y])


def draw(color):
    snowflakes_length = 15
    for i in snowflake:
        sd.snowflake(sd.get_point(i[0], i[1]), color=color, length=snowflakes_length)


def move():
    for i in snowflake:
        if i[1] < 10:
            sd.snowflake(sd.get_point(i[0], i[1]), color=sd.COLOR_WHITE, length=15)
            i[1] = 600
            continue
        i[1] -= 9
        i[0] += sd.random_number(-10, 10)


create(30)
while True:
    sd.start_drawing()
    draw(sd.background_color)
    move()
    draw(sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


