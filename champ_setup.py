import pandas as pd
import random

data = pd.read_json('champions.json')

def champ_to_guess():
    names = data.name.to_list()
    name = random.choice(names)
    return name

champion_name = champ_to_guess()

class Champion:
    def __init__(self,name):
        self.name = name
        self.lanes = data[data.name == self.name].lanes.values[0]
        self.species = data[data.name == self.name].species.values[0]
        self.resource = data[data.name == self.name].resource.values[0]
        self.range_type = data[data.name == self.name].rangeType.values[0]
        self.region = data[data.name == self.name].region.values[0]
        self.release_date = data[data.name == self.name].releaseDate.values[0]

class Guess:
    def __init__(self, name):
        self.name = name
        self.lanes = data[data.name == self.name].lanes.values[0]
        self.species = data[data.name == self.name].species.values[0]
        self.resource = data[data.name == self.name].resource.values[0]
        self.range_type = data[data.name == self.name].rangeType.values[0]
        self.region = data[data.name == self.name].region.values[0]
        self.release_date = data[data.name == self.name].releaseDate.values[0]


tomek = Champion('Ahri')
data_tomka = int(tomek.release_date[:3])
print(data_tomka)