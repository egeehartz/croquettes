from datetime import date
from movements import Swimming
from .animal import Animal

class Tadpole(Animal, Swimming): 

    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, food)
        Swimming.__init__(self)

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Goldfish: 

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Mallard: 

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Goose: 

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Frog: 

    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
        self.food = food
        self.chip_num = chip_num

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')