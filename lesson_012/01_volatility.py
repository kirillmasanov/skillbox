# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

# TODO написать код в однопоточном/однопроцессорном стиле
import os
from collections import defaultdict
import time


class Volatility:

    volatility_dict = defaultdict()
    null_dict = defaultdict()

    def __init__(self, file_name):
        self.file_name = file_name
        self.volatility = 0
        self.sum_price = 0
        self.average_price = 0
        self.min_price = 99999999
        self.max_price = 0
        self.count = 0

    def run(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            file.readline()
            for line in file:
                price = float(line.split(',')[2])
                self.sum_price += price
                self.count += 1
                if self.min_price > price:
                    self.min_price = price
                if self.max_price < price:
                    self.max_price = price
            self.average_price = self.sum_price / self.count
            self.volatility = ((self.max_price - self.min_price) / self.average_price) * 100

        f_name = os.path.basename(self.file_name)[:-4]
        if self.volatility == 0:
            Volatility.null_dict[f_name] = round(self.volatility, 2)
        else:
            Volatility.volatility_dict[f_name] = round(self.volatility, 2)


def make_file_list(scan_folder):
    file_list = []
    for dir_path, dir_name, file_name in os.walk(scan_folder):
        for file in file_name:
            file_list.append(os.path.join(dir_path, file))
    return file_list


def time_track(func, *args, **kwargs):
    started_at = time.time()

    result = func(*args, **kwargs)

    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Функция работала {elapsed} секунд(ы)')
    return result


@time_track
def main():
    file_list = make_file_list('trades')
    volatilities = [Volatility(file_name=file) for file in file_list]

    for ff in volatilities:
        ff.run()

    sort_dict = sorted(Volatility.volatility_dict.items(), key=lambda kv: kv[1], reverse=True)
    print(f'Максимальная волатильность:')
    for i in range(3):
        print(f'{sort_dict[i][0]} - {sort_dict[i][1]} %')
    print(f'Минимальная волатильность:')
    for i in range(2, -1, -1):
        print(f'{sort_dict[-i - 1][0]} - {sort_dict[-i - 1][1]} %')
    print(f'Нулевая волатильность:')
    print(', '.join(list(Volatility.null_dict.keys())))


if __name__ == '__main__':
    main()
