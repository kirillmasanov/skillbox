# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
sd.resolution = 1600, 900

p = sd.get_point(100, 100)

colour_list = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
c_list = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
print('Возможные цвета:')
for key, value in enumerate(colour_list):
    print(f'{key}: {value}')

choice = int(input('Выберите цвет:'))


def polygon(angle_num, point, angle=0, length=100):
    angle_n = 180 - round(((angle_num - 2)/angle_num), 15) * 180
    for i in range(angle_num):
        if i == angle_num - 1:
            sd.line(point, p, width=3, color=c_list[choice])
            break
        v = sd.get_vector(start_point=point, angle=angle + i * angle_n, length=length, width=3)
        v.draw(color=c_list[choice])
        print(colour_list[choice])
        point = v.end_point

polygon(5, p)

sd.pause()
