class PettingZoo:

    def __init__(self, name):
        super().__init__(name)
        self.description = "cute and fuzzy critters to cuddle"
    
    def add_to_list(self, animal):
        self.animals.append(animal)