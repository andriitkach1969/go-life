from src.Constants import IS_SUITABLE, IS_PLEASURE, IS_UNPLEASURE

IS_DESERT = 3
IS_CROWD = 2

class Moore:

    def __init__(self):
        pass

    def get_neighbors_state(self):
        pass

    def get_comfort_level(self):
        if self.get_neighbors_state() == IS_SUITABLE:
            return IS_PLEASURE
        return IS_UNPLEASURE

