class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()
    
    def add_to_list(self, animal):
        self.animals.append(animal)
        

class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "slithering snakes so satisfyingly sneaky"
        self.animals = list()
    
    def add_to_list(self, animal):
        self.animals.append(animal)

class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "Stroll by the pond!"
        self.animals = list()
    
    def add_to_list(self, animal):
        self.animals.append(animal)
    
