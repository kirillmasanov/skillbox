# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    def __str__(self):
        return 'поле имени содержит НЕ только буквы'


class NotEmailError(Exception):
    def __str__(self):
        return 'поле емейл НЕ содержит @ и .(точку)'


def check_line(line: str):
    name, mail, age = line.split(' ')
    for ch in name:
        if not ch.isalpha():
            raise NotNameError
        elif '@' and '.' not in mail:
            raise NotEmailError
        elif not 10 <= int(age) <= 99:
            raise ValueError('Возраст не соответствует!')
    with open('registrations_good.txt', 'a', encoding='utf-8') as good_log:
        good_log.write(line + '\n')


with open('registrations.txt', 'r', encoding='utf-8') as ff:
    for line in ff:
        line = line.rstrip()
        try:
            check_line(line)
        except (ValueError, NotNameError, NotEmailError) as exc:
            print(f'Ошибка: {exc}: {line}')
            with open('registrations_bad.txt', 'a', encoding='utf-8') as bad_log:
                bad_log.write(f'{line} : Ошибка: {exc} \n')
