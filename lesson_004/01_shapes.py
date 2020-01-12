# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1600, 900
# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()

# def triangle(point, angle=0, width: str=3):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=width)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=width)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=width)
#     v3.draw()
#
p_triangle = sd.get_point(100, 100)


def triangle(point_triangle, angle=0, length=200):
    for i in range(3):
        v = sd.get_vector(start_point=point_triangle, angle=angle + i * 120, length=length, width=3)
        v.draw()
        point_triangle = v.end_point


triangle(p_triangle)

p_square = sd.get_point(500, 100)


def square(point_square, angle=0, length=200):
    for i in range(4):
        v = sd.get_vector(start_point=point_square, angle=angle + i * 90, length=length, width=3)
        v.draw()
        point_square = v.end_point


square(p_square)

p_pentagon = sd.get_point(800, 100)


def pentagon(point_pentagon, angle=0, length=200):
    for i in range(5):
        v = sd.get_vector(start_point=point_pentagon, angle=angle + i * 72, length=length, width=3)
        v.draw()
        point_pentagon = v.end_point


pentagon(p_pentagon)

p_hexagon = sd.get_point(1200, 100)


def hexagon(point_hexagon, angle=0, length=200):
    for i in range(6):
        v = sd.get_vector(start_point=point_hexagon, angle=angle + i * 60, length=length, width=3)
        v.draw()
        point_hexagon = v.end_point

p = sd.get_point(500, 500)
def polygon(angle_num, point, angle=0, length=100):
    angle_n = 180 - round(((angle_num - 2)/angle_num), 15) * 180
    for i in range(angle_num):
        if i == angle_num - 1:
            sd.line(point, p, width=3)
            break
        v = sd.get_vector(start_point=point, angle=angle + i * angle_n, length=length, width=3)
        v.draw()
        point = v.end_point



# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
