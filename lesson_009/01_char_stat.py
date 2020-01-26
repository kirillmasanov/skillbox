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

    def dict_word(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            my_dict = {}
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char not in my_dict:
                            my_dict[char] = 1
                        else:
                            my_dict[char] += 1
        return my_dict

    def sort_key_alpha_up(self):
        sort_key = sorted(self.dict_word())
        return sort_key

    def print_dict(self, sort_key, my_dict):
        sum_rate = 0
        print(f'+{"+":-^20}+')
        print(f'|{"буква": ^9}|{"частота": ^10}|')
        print(f'+{"+":-^20}+')
        for key in sort_key:
            print(f'|{key: ^9}|{my_dict[key]: ^10}|')
            sum_rate += my_dict[key]
        print(f'+{"+":-^20}+')
        print(f'|{"итого": ^9}|{sum_rate: ^10}|')
        print(f'+{"+":-^20}+')


book1 = CharStat(file_name='voyna-i-mir.txt')
my_dict = book1.dict_word()

sort_key = book1.sort_key_alpha_up()
book1.print_dict(sort_key=sort_key, my_dict=my_dict)




# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
