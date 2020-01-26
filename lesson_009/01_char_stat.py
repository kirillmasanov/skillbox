# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class CharStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.my_dict = {}
        self.sorted_key = []
        self.rate = []

    def dict_word(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char not in self.my_dict:
                            self.my_dict[char] = 1
                        else:
                            self.my_dict[char] += 1

    def sort_key_alpha_up(self):
        self.sorted_key = sorted(self.my_dict)

    def sort_key_alpha_down(self):
        self.sorted_key = sorted(self.my_dict, reverse=True)

    def sort_rate_up(self):
        self.rate = sorted(list(self.my_dict.values()))

    def print_dict(self):
        sum_rate = 0
        print(f'+{"+":-^20}+')
        print(f'|{"буква": ^9}|{"частота": ^10}|')
        print(f'+{"+":-^20}+')
        for key in self.sorted_key:
            print(f'|{key: ^9}|{self.my_dict[key]: ^10}|')
            sum_rate += self.my_dict[key]
        print(f'+{"+":-^20}+')
        print(f'|{"итого": ^9}|{sum_rate: ^10}|')
        print(f'+{"+":-^20}+')

    def print_dict_rate(self):
        sum_rate = 0
        print(f'+{"+":-^20}+')
        print(f'|{"буква": ^9}|{"частота": ^10}|')
        print(f'+{"+":-^20}+')
        for value in self.rate:
            for key in self.my_dict:
                if self.my_dict[key] == value:
                    print(f'|{key: ^9}|{value: ^10}|')
                    sum_rate += value
        print(f'+{"+":-^20}+')
        print(f'|{"итого": ^9}|{sum_rate: ^10}|')
        print(f'+{"+":-^20}+')


book1 = CharStat(file_name='voyna-i-mir.txt')
book1.dict_word()
# book1.sort_key_alpha_down()
# book1.sort_key_alpha_up()
# book1.print_dict()
book1.sort_rate_up()
book1.print_dict_rate()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
