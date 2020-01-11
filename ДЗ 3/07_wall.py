# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
point1 = sd.get_point(0,0)
point2 = sd.get_point(100,50)
# TODO здесь ваш код
for i in range(20):

    for j in range(0, 501, 50):
        m = j % 100
        sd.rectangle(left_bottom=sd.get_point(0+m,j), right_top=sd.get_point(100*i+m,50+j), color=sd.COLOR_YELLOW, width=2)


sd.pause()
