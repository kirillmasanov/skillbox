# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    def __str__(self):
        return 'IamGodError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


class SuicideError(Exception):
    def __str__(self):
        return 'SuicideError'


exc_dict = {'1': IamGodError(), '2': DrunkError(), '3': CarCrashError,
            '4': GluttonyError, '5': DepressionError, '6': SuicideError}


def one_day():
    dice = randint(1, 13)
    dice_exc = str(randint(1, 6))
    if dice == 13:
        raise exc_dict[dice_exc]
    return randint(1, 7)


total_karma = 0
total_exc = 0
while total_karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        total_karma += one_day()
        # print(total_karma)
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        print(f'Поймано - {exc}')
        total_exc += 1
print(total_karma)
print(f'Всего поймано - {total_exc}')