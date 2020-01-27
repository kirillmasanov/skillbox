# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class LogParserMin:
    def __init__(self, file_name, file_output):
        self.file_name = file_name
        self.file_output = file_output
        self.dict_min = {}

    def calc_file(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if line[-4] == 'N':
                    if line[:17] + ']' not in self.dict_min:
                        self.dict_min[line[:17] + ']'] = 1
                    else:
                        self.dict_min[line[:17] + ']'] += 1

    def print_dict(self):
        with open(self.file_output, 'w') as file:
            for key, value in self.dict_min.items():
                file.write(f'{key} {value}\n')


class LogParserHour(LogParserMin):
    def calc_file(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if line[-4] == 'N':
                    if line[:14] + ']' not in self.dict_min:
                        self.dict_min[line[:14] + ']'] = 1
                    else:
                        self.dict_min[line[:14] + ']'] += 1


class LogParserMonth(LogParserMin):
    def calc_file(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if line[-4] == 'N':
                    if line[:8] + ']' not in self.dict_min:
                        self.dict_min[line[:8] + ']'] = 1
                    else:
                        self.dict_min[line[:8] + ']'] += 1


class LogParserYear(LogParserMin):
    def calc_file(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if line[-4] == 'N':
                    if line[:5] + ']' not in self.dict_min:
                        self.dict_min[line[:5] + ']'] = 1
                    else:
                        self.dict_min[line[:5] + ']'] += 1


my_parser = LogParserHour(file_name='events.txt', file_output='events_output.txt')
my_parser.calc_file()
my_parser.print_dict()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
