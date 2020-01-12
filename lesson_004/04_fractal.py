# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1500, 800)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
point_0 = sd.get_point(750, 5)


# def branch(point, angle, length, delta=30):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * .75
#     branch(point=next_point, angle=next_angle, length=next_length, delta=delta)

def draw_branch(point, angle, length):
    if length < 5:
        return
    delta_angle = 30 * (100 - sd.random_number(1, 40))/100
    delta_length = (100 - sd.random_number(1, 20))/100
    v1 = sd.get_vector(start_point=point, angle=angle-delta_angle, length=length, width=1)
    v1.draw()
    next_point1 = v1.end_point

    v2 = sd.get_vector(start_point=point, angle=angle+delta_angle, length=length, width=1)
    v2.draw()
    next_point2 = v2.end_point

    next_angle = angle
    next_length = length * .8 * delta_length
    draw_branch(point=next_point1, angle=next_angle-delta_angle, length=next_length)
    draw_branch(point=next_point2, angle=next_angle+delta_angle, length=next_length)


draw_branch(point_0, angle=90, length=200)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


