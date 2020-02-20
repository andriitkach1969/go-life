from array import array
import random


class Earth:

    RowSize = 100
    ColumnSize = 100
    MyArray = array('H')

    def __init__(self, nsize, msize):
        self.RowSize = nsize
        self.ColumnSize = msize
        self.MyArray = array('H', (False for s in range(self.RowSize * self.ColumnSize)))

    def get(self, row_pos, column_pos):

        row_pos = row_pos % self.RowSize
        column_pos = column_pos % self.ColumnSize
        return self.MyArray[row_pos * self.ColumnSize + column_pos]

    def set(self, row_pos, column_pos):
        self.MyArray[row_pos * self.ColumnSize + column_pos] = True

    def unset(self, row_pos, column_pos):
        self.MyArray[row_pos * self.ColumnSize + column_pos] = False

    def init_life(self, density):
        for i in range(self.RowSize):
            for j in range(self.ColumnSize):
                if random.randint(1, density) == density:
                    self.set(i, j)

    def get_neighbors(self, row_pos, column_pos, method):

        res = []

        if method == "moore":
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 2 - abs(i)):
                    res.append(self.get(row_pos + i, column_pos + j))
        return res

    def get_neighbors_count(self, row_pos, row_column, method):

        neighbors = self.get_neighbors(row_pos, row_column, method)
        count = 0
        for item in neighbors:
            if item:
                count += 1
        return count

    def next_generation(self):

        for i in range(self.RowSize):
            for j in range(self.ColumnSize):

                current_neighbors = self.get_neighbors_count(i, j, "moore")
                alive = self.get(i, j)
                if alive and (current_neighbors < 2 or current_neighbors > 3):
                    self.unset(i, j)
                if not alive and current_neighbors == 3:
                    self.set(i, j)

    def print_generation(self):
        for i in range(self.RowSize):
            for j in range(self.ColumnSize):
                print(self.get(i, j), end=' ')
            print()
