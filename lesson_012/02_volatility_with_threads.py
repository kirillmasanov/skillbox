# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле
import os
import threading
from collections import defaultdict
import time


class Volatility(threading.Thread):

    volatility_dict = defaultdict()
    null_dict = defaultdict()

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        ff.start()
    for ff in volatilities:
        ff.join()

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