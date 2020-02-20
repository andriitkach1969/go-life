from array import array
import random

class Earth:

    RowSize = 100
    ColumnSize = 100
    MyArray = array('H')

    def __init__(self, nsize, msize, lifeRule = None):
        self.lifeRule = lifeRule
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

    def next_generation(self):

        for i in range(self.RowSize):
            for j in range(self.ColumnSize):
                alive = self.get(i, j)
                comfort_level = lifeRule.get_comfort_level();
                if alive and comfort_level = IS_UNPLEASURE:
                    self.unset(i, j)
                if not alive and comfort_level = IS_PLEASURE:
                    self.set(i, j)
