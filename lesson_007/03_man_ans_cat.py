# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
# =======================================================================================


class House:
    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return f'В доме еды осталось {self.food}, денег осталось {self.money}'


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='yellow')
            self.fullness += 20
            self.house.food -= 5
        else:
            cprint(f'{self.name} нет еды', color='red')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.house.money += 150
        self.fullness -= 10

    def play(self):
        cprint(f'{self.name} играл целый день', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин за едой', color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint(f'{self.name} деньги кончились!', color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} Вьехал в дом', color='cyan')

    def pick_cat(self, name):
        cat = Cat(name)
        cat.go_to_the_house(self.house)


    def buy_cat_food(self):
        self.house.cat_food += 50
        self.house.money -= 50

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint(f'{self.name} убирался в доме весь день', color='green')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return
        dice = randint(1, 7)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.clean_house()
        else:
            self.play()


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'

    def cat_sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} спал весь день', color='green')

    def cat_eat(self):
        self.fullness += 20
        self.house.cat_food -= 5
        cprint(f'{self.name} ел весь день', color='green')

    def tear_wallpapers(self):
        self.fullness -= 10
        self.house.dirt -= 5
        cprint(f'{self.name} драл обои весь день', color='green')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} Вьехал в дом', color='cyan')
        citizens.append(self)

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return
        dice = randint(1, 2)
        if self.fullness < 20:
            self.cat_eat()
        elif dice == 1:
            self.cat_sleep()
        elif dice == 2:
            self.tear_wallpapers()


citizens = [
    Man(name='Вася')
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
citisen.pick_cat('Лаврентий')
for day in range(1, 366):
    print(len(citizens))
    print(f'================ день {day} ==================')
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)
