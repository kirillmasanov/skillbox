import json
import sys
from pprint import pprint


class DungeonRPG:

    def __init__(self, file):
        self.file = file
        self.remaining_time = '1234567890.0987654321'
        self.current_loc = ''
        self.current_experience = ''
        self.current_date = ''
        self.current_locations = {'monster': [], 'next_loc': []}

    def load_file(self):
        with open(self.file, 'r') as read_file:
            loaded_json_map = json.load(read_file)
        return loaded_json_map

    def attack_monster(self):
        if len(self.current_locations['monster']) > 1:
            pass
        else:
            print(f'Монстр убит')
            self.current_locations['monster'] = 0

    def choose_action(self):
        while True:
            action = int(input('> '))
            if action == 1:
                # attack the monster
                self.attack_monster()
                return 1
            elif action == 2:
                # go to the next location
                return 2
            elif action == 3:
                sys.exit()
            else:
                print('Введите 1, 2 или 3!')

    def run(self):
        map_remaining = self.load_file()
        for loc in map_remaining.keys():
            print(f'Вы находитесь в {loc}')
            print(f'Внутри вы видите:')
            for val in map_remaining[loc]:
                if type(val) == dict:
                    for key in val.keys():
                        self.current_locations['next_loc'].append(key)
                        print(f'-- Вход в локацию: {key}')
                else:
                    self.current_locations['monster'].append(val)
                    print(f'-- Монстра {val}')
        print()
        print(f'Выберите действие: ')
        print(f'1.Атаковать монстра')
        print(f'2.Перейти в другую локацию')
        print(f'3.Выход')
        # action = int(input('> '))
        self.choose_action()

        print(self.current_locations)

        pprint(map_remaining)

rpg = DungeonRPG('rpg.json')
rpg.run()
