from .attractions import Attraction


class Wetlands(Attraction):

    def __init__(self, name):
        super().__init__(name)
        self.description = "Stroll by the pond!"
    
    def add_to_list(self, animal):
        self.animals.append(animal)
    
    @property
    def last_critter_added(self):
        return self.animals[-1]