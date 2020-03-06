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

    def current_location(self):
        map_remaining = self.load_file()
        loc_list = list(map_remaining.keys())
        self.current_loc = loc_list[0]

    def run(self):
        self.current_location()

        print(self.current_loc)


        # pprint(map_remaining)

rpg = DungeonRPG('rpg.json')
rpg.run()
