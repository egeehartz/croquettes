from datetime import date


class Snake: 

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed_print(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Turtle: 

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Lizard: 

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Viper: 

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Boa: 

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')