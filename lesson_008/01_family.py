# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dust = 0
        self.cat_food = 30

    def __str__(self):
        return f'Дом: деньги - {self.money}, еда - {self.food}, пыль - {self.dust}'


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30

    def __str__(self):
        return f'{self.name} - сытость {self.fullness}'

    def eat(self):
        cat_food_quon = randint(1, 10)
        home.cat_food -= cat_food_quon
        self.fullness += cat_food_quon * 2
        return print(f'{self.name} поел!')

    def sleep(self):
        self.fullness -= 10
        return print(f'{self.name} спал весь день!')

    def soil(self):
        self.fullness -= 10
        home.dust += 5
        return print(f'{self.name} драл обои!')

    def act(self):
        dice = randint(1, 5)
        if self.fullness < 0:
            return cprint(f'{self.name} умер от голода!', color='yellow')
        if dice == 1:
            self.sleep()
        elif dice == 2:
            self.soil()
        else:
            self.eat()


class Human:
    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.earn_money = 0
        self.food_eaten = 0
        self.coats = 0

    def __str__(self):
        return f'{self.name} - сытость {self.fullness}, счастье {self.happiness}'

    def eat(self):
        food_quan = randint(20, 30)
        self.fullness += food_quan
        home.food -= food_quan
        self.food_eaten += food_quan
        return print(f'{self.name} поел!')

    def pet_the_cat(self):
        self.happiness += 5
        return print(f'{self.name} погладил кота!')


class Child(Human):

    def __init__(self, name):
        super().__init__(name)
        self.fullness = 100

    def __str__(self):
        return f'{self.name} - сытость {self.fullness}'

    def eat(self):
        home.food -= randint(1, 10)
        return print(f'{self.name} покушал!')

    def sleep(self):
        return print(f'{self.name} поспал!')

    def act(self):
        dice = randint(1, 2)
        if dice == 1:
            self.sleep()
        else:
            self.eat()

class Husband(Human):

    def work(self):
        self.earn_money += 150
        home.money += 150
        self.fullness -= 10
        return print(f'{self.name} сходил на работу!')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        return print(f'{self.name} играл в WoT!')

    def buy_cat_food(self):
        home.money -= 30
        home.cat_food += 30
        return print(f'{self.name} купил кошачий корм!')

    def act(self):
        dice = randint(1, 2)
        if home.dust > 90:
            self.happiness -= 10
        if self.fullness < 0:
            return cprint(f'{self.name} умер от голода!', color='yellow')
        if self.happiness < 10:
            return cprint(f'{self.name} умер от депрессии!', color='yellow')
        if self.fullness < 40 and home.food > 5:
            self.eat()
        elif home.money < 100:
            self.work()
        elif home.cat_food <= 30:
            self.buy_cat_food()
        elif dice == 1:
            self.gaming()
        else:
            self.pet_the_cat()


class Wife(Human):

    def shopping(self):
        home.money -= 40
        home.food += 40
        self.fullness -= 10
        return print(f'{self.name} сходила в магазин!')

    def buy_fur_coat(self):
        self.happiness += 60
        home.money -= 350
        self.fullness -= 10
        self.coats += 1
        return print(f'{self.name} купила шубу!')

    def clean_house(self):
        self.fullness -= 10
        home.dust -= randint(50, 100)
        return print(f'{self.name} убралась в доме!')

    def act(self):
        dice = randint(1, 4)
        if self.fullness < 0:
            return cprint(f'{self.name} умер от голода!', color='yellow')
        if self.happiness < 10:
            return cprint(f'{self.name} умер от депрессии!', color='yellow')
        if home.dust > 90:
            self.happiness -= 10
            self.clean_house()
        elif self.fullness < 40 and home.food > 5:
            self.eat()
        elif home.food < 100 and home.money > 40:
            self.shopping()
        elif dice == 1 and home.money > 350:
            self.buy_fur_coat()
        elif dice == 2:
            self.pet_the_cat()
        else:
            self.shopping()


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
barsik = Cat(name='Барсик')
kolya = Child(name='Коля')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.dust += 5
    serge.act()
    masha.act()
    kolya.act()
    barsik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(barsik, color='cyan')
    cprint(home, color='cyan')

cprint(f'Заработано - {serge.earn_money}, \
съедено еды - {serge.food_eaten + masha.food_eaten}, куплено шуб - {masha.coats}', color='magenta')


# TODO после реализации первой части - отдать на проверку учителю


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

