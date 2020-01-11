# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
point1 = sd.get_point(50,50)
point2 = sd.get_point(350,450)
step = 20

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
for i in range(1, 7):
    sd.line(start_point=sd.get_point(50 + i * step,50),
            end_point=sd.get_point(350 + i * step,450),
            color=rainbow_colors[i], width=4)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
for i in range(1, 7):
    sd.circle(center_position=sd.get_point(500,-500), radius=(900+i*step), color=rainbow_colors[i], width=20)

sd.pause()
