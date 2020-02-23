from array import array
import random
from tkinter import Canvas

from src.Constants import IS_PLEASURE, IS_UNPLEASURE


class Earth:
    DELAY_STEP = 10

    def __init__(self, nsize, msize, scale, dencity=None, lifeRule=None, root=None):
        self.root = root
        self.lifeRule = lifeRule
        self.RowSize = nsize
        self.ColumnSize = msize
        self.Scale = scale
        self.dencity = dencity
        self.drawArray = []
        self.MyArray = array('H', (False for s in range(self.RowSize * self.ColumnSize)))
        self.canvas = Canvas(root, width=self.RowSize*self.Scale, height=self.ColumnSize*self.Scale, bg="black")
        self.canvas.pack()
        self.delay = 10
        self.__init_life()

    def delay_increase(self):
        self.delay += self.DELAY_STEP

    def delay_decrease(self):
        if self.delay > 0:
            self.delay -= self.DELAY_STEP

    def get(self, row_pos, column_pos):
        row_pos = row_pos % self.RowSize
        column_pos = column_pos % self.ColumnSize
        return self.MyArray[row_pos * self.ColumnSize + column_pos]

    def __set(self, row_pos, column_pos):
        self.MyArray[row_pos * self.ColumnSize + column_pos] = True
        self.canvas.itemconfigure(self.drawArray[row_pos * self.ColumnSize + column_pos], fill='yellow')

    def __unset(self, row_pos, column_pos):
        self.MyArray[row_pos * self.ColumnSize + column_pos] = False
        self.canvas.itemconfigure(self.drawArray[row_pos * self.ColumnSize + column_pos], fill='black')

    def __init_life(self):
        for i in range(self.RowSize):
            for j in range(self.ColumnSize):
                self.drawArray.append(self.canvas.create_oval(
                    i * self.Scale, j * self.Scale,
                    i * self.Scale + self.Scale,
                    j * self.Scale + self.Scale, fill='black'))
        for i in range(self.RowSize):
            for j in range(self.ColumnSize):
                if random.randint(1, self.dencity) == self.dencity:
                    self.__set(i, j)

    def __next_generation(self):
        for i in range(self.RowSize):
            for j in range(self.ColumnSize):
                alive = self.get(i, j)
                comfort_level = self.lifeRule(self, self.RowSize, self.ColumnSize, i, j)
                if alive and comfort_level == IS_UNPLEASURE:
                    self.__unset(i, j)
                if not alive and comfort_level == IS_PLEASURE:
                    self.__set(i, j)

    def next_move(self):
        self.__next_generation()
        self.canvas.after(self.delay, self.next_move)
