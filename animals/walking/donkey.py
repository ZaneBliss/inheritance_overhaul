from ..animal import Animal

class Donkey(Animal): 
    
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.walking = True
        self.shift = shift