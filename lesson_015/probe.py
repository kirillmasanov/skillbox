from datetime import datetime, timedelta
import time
import json
import re
import sys
from decimal import Decimal


class DungeonRPG:

    def __init__(self, file):
        self.file = file
        self.remaining_time = '1234567890.0987654321'
        self.current_experience = 0
        self.current_date = 0
        self.location_name = ''
        self.list_monsters = []
        self.list_locations = []
        self.map = {}
        self.key = True

    def load_file(self):
        with open(self.file, 'r') as read_file:
            self.map = json.load(read_file)

    def parse_location(self):
        for loc in self.map.keys():
            self.location_name = loc
            for val in self.map[loc]:
                if type(val) == dict:
                    for key in val.keys():
                        self.list_locations.append(key)
                elif type(val) == list:
                    for n in val:
                        self.list_monsters.append(n)
                else:
                    self.list_monsters.append(val)

    def time_count(self, time_object):
        time_elapsed = Decimal(re.search(r'tm\d+', time_object)[0][2:])
        self.remaining_time = Decimal(self.remaining_time) - time_elapsed
        self.current_date += time_elapsed

    def monster_count(self, monster_name):
        exp_received = int(re.search(r'exp\d+', monster_name)[0][3:])
        self.current_experience += exp_received
        self.time_count(monster_name)
        print(f'Получено опыта - {exp_received}, всего - {self.current_experience}')

    def monster_attack(self):
        if len(self.list_monsters) > 1:
            for i in range(len(self.list_monsters)):
                print(f'{i + 1} - Атаковать монстра {self.list_monsters[i]}')
            print('Выберити монстра, чтобы атаковать:')
            choice = int(input('> '))
        else:
            choice = 1
        monster_killed = self.list_monsters.pop(choice - 1)
        print(f'Монстр {monster_killed} повержен!')
        self.monster_count(monster_killed)
        self.key = False

    def choose_action(self):
        if len(self.list_locations) > 0 or len(self.list_monsters) > 0:
            print(f'Выберите действие: ')
        if len(self.list_locations) == 0:
            if len(self.list_monsters) == 0:
                print('Поздравляем вы прошли подземелье!')
                sys.exit()
            print(f'1.Атаковать монстра')
            print(f'2.Выход')
            print('>>> Это последняя комната! <<<')
            while True:
                action = int(input('> '))
                if action == 1:
                    self.monster_attack()
                    return
                elif action == 2:
                    sys.exit()
                else:
                    print('Введите 1 или 2!')
        elif len(self.list_monsters) == 0:
            print(f'1.Перейти в другую локацию')
            print(f'2.Выход')
            while True:
                action = int(input('> '))
                if action == 1:
                    self.change_location()
                    return
                elif action == 2:
                    sys.exit()
                else:
                    print('Введите 1 или 2!')

        else:
            print(f'1.Атаковать монстра')
            print(f'2.Перейти в другую локацию')
            print(f'3.Выход')
            while True:
                action = int(input('> '))
                if action == 1:
                    self.monster_attack()
                    return
                elif action == 2:
                    self.change_location()
                    return
                elif action == 3:
                    sys.exit()
                else:
                    print('Введите 1, 2 или 3!')

    def change_location(self):
        if len(self.list_locations) > 1:
            for i in range(len(self.list_locations)):
                print(f'{i + 1} - Перейти в локацию {self.list_locations[i]}')
            print('Выберити локацию для перехода:')
            choice = int(input('> '))
        else:
            choice = 1
        next_location = self.list_locations[choice - 1]
        for pos in self.map[self.location_name]:
            if type(pos) == dict:
                if pos.get(next_location):
                    self.map = pos
        self.key = True
        self.location_name = next_location
        self.time_count(self.location_name)
        self.list_locations = []
        self.list_monsters = []

    def run(self):
        while True:
            if self.key:
                self.parse_location()
            if len(self.list_locations) > 0 or len(self.list_monsters) > 0:
                print(f'Вы находитесь в {self.location_name}')
                print(f'У вас {self.current_experience} опыта и осталось {self.remaining_time} секунд')
                print(timedelta(seconds=int(self.current_date)))
                print(f'Внутри вы видите:')
            for loc in self.list_monsters:
                print(f'-- Монстра: {loc}')
            for loc in self.list_locations:
                print(f'-- Вход в локацию: {loc}')

            self.choose_action()
            print('*' * 50)


rpg = DungeonRPG('rpg.json')
rpg.load_file()
rpg.run()
