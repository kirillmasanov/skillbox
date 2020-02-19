# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import argparse
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(description='Билет на самолет')
parser.add_argument('--fio', action="store", dest="fio", default='Marianna')
parser.add_argument('--from_', action="store", dest="from_", default='Moscow')
parser.add_argument('--to', action="store", dest="to", default='Bali')
parser.add_argument('--date', action="store", dest="date", default='20.02')
args = parser.parse_args()


def make_ticket(fio, from_, to, date):
    im = Image.open('images/ticket_template.png')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('fonts/arial.ttf', size=16)
    draw.text((45, 122), fio, font=font, fill='black')
    draw.text((45, 192), from_, font=font, fill='black')
    draw.text((45, 257), to, font=font, fill='black')
    draw.text((283, 257), date, font=font, fill='black')
    im.show()


make_ticket(args.fio, args.from_, args.to, args.date)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
