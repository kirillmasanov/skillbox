# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def bubble(point, step):
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(point, radius=radius, width=2)


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код


# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
# for y in range(100, 401, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=10)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for i in range(100):
    point = sd.random_point()
    bubble(point=point, step=10)
sd.pause()


