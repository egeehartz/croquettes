#parent class

from datetime import date

class Animal:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food