from attractions.Attraction import Attraction

class SnakePit(Attraction):

    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)
        self.underbrush = True