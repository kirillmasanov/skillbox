# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def gen_parser():
    key = True
    with open('events.txt', 'r', encoding='utf8') as file:
        min_list = {}
        for line in file:
            a = line[-4]
            b = line[1:17]
            if a == 'N':
                if b not in min_list:
                    if key == False:
                        for c, d in min_list.items():
                            yield c, d
                        min_list = {}
                    min_list[b] = 1
                    # print(min_list[b])
                else:
                    min_list[b] += 1
                    # print(min_list[b])
                    key = False


grouped_events = gen_parser()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
