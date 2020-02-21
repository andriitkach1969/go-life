from src.Constants import IS_PLEASURE, IS_UNPLEASURE
IS_OK = 0
IS_DESERT = 1
IS_CROWD = 2


class Moore:

    def __init__(self):
        self.array = 0
        self.nsize = 0
        self.msize = 0
        self.row_pos = 0
        self.column_pos = 0

    def __get_neighbors(self, arr):
        res = []

        for i in range(-1, 2, 1):
            for j in range(-1, 2, 2 - abs(i)):
                res.append(arr.get(self.row_pos + i, self.column_pos + j))
        return res

    def __get_neighbors_state(self, arr):
        neighbors = self.__get_neighbors(arr)
        count = 0
        for item in neighbors:
            if item:
                count += 1
        if count < 2:
            return IS_DESERT
        elif count > 3:
            return IS_CROWD
        elif count == 3:
            return IS_OK

    def get_comfort_level(self, arr, nsize, msize, i, j):
        self.row_pos = i
        self.column_pos = j
        self.nsize = nsize
        self.msize = msize
        state = self.__get_neighbors_state(arr)
        if state == IS_OK:
            return IS_PLEASURE
        elif state == IS_CROWD or state == IS_DESERT:
            return IS_UNPLEASURE

