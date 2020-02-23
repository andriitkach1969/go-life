from src.Constants import IS_PLEASURE, IS_UNPLEASURE
IS_OK = 0
IS_DESERT = 1
IS_CROWD = 2


class Neumann:

    def __init__(self):
        self.array = 0
        self.nsize = 0
        self.msize = 0

    def __get_neighbors(self, arr, current_i, current_j):
        res = []
        nw = arr.get(current_i - 1 if current_i > 1 else self.nsize, current_j - 1 if current_j > 1 else self.msize)
        n = arr.get(current_i - 1 if current_i > 1 else self.nsize, current_j)
        ne = arr.get(current_i - 1 if current_i > 1 else self.nsize, current_j + 1 if current_j < self.msize else 1)
        w = arr.get(current_i, current_j - 1 if current_j > 1 else self.msize)
        e = arr.get(current_i, current_j + 1 if current_j < self.msize else 1)
        sw = arr.get(current_i + 1 if current_i < self.nsize else 1, current_j - 1 if current_j > 1 else self.msize)
        s = arr.get(current_i + 1 if current_i < self.nsize else 1, current_j)
        se = arr.get(current_i + 1 if current_i < self.nsize else 1, current_j + 1 if current_j < self.msize else 1)
        res = [n, e, w, s]
        return res

    def __get_neighbors_state(self, arr, current_i, current_j):
        neighbors = self.__get_neighbors(arr, current_i, current_j)
        count = 0
        for item in neighbors:
            if item:
                count += 1
        if count < 3:
            return IS_DESERT
        elif count > 3:
            return IS_CROWD
        elif count == 3:
            return IS_OK

    def get_comfort_level(self, arr, nsize, msize, current_i, current_j):
        self.nsize = nsize
        self.msize = msize
        state = self.__get_neighbors_state(arr, current_i, current_j)
        if state == IS_OK:
            return IS_PLEASURE
        elif state == IS_CROWD or state == IS_DESERT:
            return IS_UNPLEASURE

