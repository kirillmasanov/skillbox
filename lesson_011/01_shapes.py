# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    if n == 3:
        def draw_polygon(point, angle, length):
            for i in range(3):
                v = sd.get_vector(start_point=point, angle=angle + i * 120, length=length, width=3)
                v.draw()
                point = v.end_point
    elif n == 4:
        def draw_polygon(point, angle, length):
            for i in range(4):
                v = sd.get_vector(start_point=point, angle=angle + i * 90, length=length, width=3)
                v.draw()
                point = v.end_point
    elif n == 5:
        def draw_polygon(point, angle, length):
            for i in range(5):
                v = sd.get_vector(start_point=point, angle=angle + i * 72, length=length, width=3)
                v.draw()
                point = v.end_point
    else:
        raise Exception('Я могу сделать умножители только на 3, 4, 5!')
    return draw_polygon


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

draw_square = get_polygon(n=4)
draw_square(point=sd.get_point(200, 200), angle=13, length=100)

draw_pentagon = get_polygon(n=5)
draw_pentagon(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
