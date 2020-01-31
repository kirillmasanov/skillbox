# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class FileArrange:
    def __init__(self, scan_folder, final_folder):
        self.scan_folder = scan_folder
        self.final_folder = final_folder
        self.file_list = []
        self.file_dict = {}

    def make_file_list(self):
        for dir_path, dir_name, file_name in os.walk(self.scan_folder):
            for file in file_name:
                self.file_list.append(os.path.join(dir_path, file))

    def make_file_dict(self):
        for file in self.file_list:
            self.file_dict[file] = time.gmtime(os.path.getmtime(file))[0:3]

    def make_arrange(self):
        for file, date in self.file_dict.items():
            final_dist = os.path.join('icons_by_year', str(date[0]), f'{date[1]:02d}')
            os.makedirs(final_dist, exist_ok=True)
            shutil.copy2(file, final_dist)


path_in = 'icons'
path_out = 'icons_by_year'
my_folder = FileArrange(scan_folder=os.path.normpath(path_in), final_folder=os.path.normpath(path_out))
my_folder.make_file_list()
my_folder.make_file_dict()
my_folder.make_arrange()
print('New folder with arranged files has been created!')

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
