from src.Constants import IS_PLEASURE, IS_UNPLEASURE
IS_OK = 0
IS_DESERT = 1
IS_CROWD = 2

class Moore:

    def __init__(self):
        self.array = None
        self.nsize = None
        self.msize = None
        self.row_pos = 0
        self.column_pos = 0

    def __get_neighbors(self):
        res = []

        for i in range(-1, 2, 1):
            for j in range(-1, 2, 2 - abs(i)):
                res.append(self.array.get(self.row_pos + i, self.column_pos + j))
        return res

    def __get_neighbors_state(self):
        neighbors = self.__get_neighbors()
        count = 0
        for item in neighbors:
            if item:
                count += 1
        if count < 2:
            return IS_DESERT
        elif count > 3:
            return IS_CROWD
        else:
            return IS_OK

    def get_comfort_level(self, array, nsize, msize, i, j):
        self.row_pos = i
        self.column_pos = j
        self.nsize = nsize
        self.msize = msize
        self.array = array
        state = self.__get_neighbors_state()
        if state == IS_OK:
            return IS_PLEASURE
        elif state == IS_CROWD or state == IS_DESERT:
            return IS_UNPLEASURE

