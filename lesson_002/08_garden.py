#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# 1 - создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
print(f'garden_set - {garden_set}')
print(f'meadow_set - {meadow_set}')
# TODO здесь ваш код
garden_set1 = garden_set | meadow_set
print()
print(f'1) {garden_set1}')

# 2 - выведите на консоль все виды цветов
# TODO здесь ваш код
garden_set2 = garden_set | meadow_set
print(f'2) {garden_set2}')

# 3 - выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
garden_set3 = garden_set & meadow_set
print(f'3) {garden_set3}')

# 4 - выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
garden_set4 = garden_set - meadow_set
print(f'4) {garden_set4}')

# 5 - выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
garden_set5 = meadow_set - garden_set
print(f'5) {garden_set5}')

