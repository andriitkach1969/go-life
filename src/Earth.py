from array import array
import random
from tkinter import Canvas

from src.Constants import IS_PLEASURE, IS_UNPLEASURE


class Earth:

    MyArray = array('H')

    def __init__(self, nsize, msize, scale, dencity, lifeRule = None, root = None):
        self.root = root
        self.lifeRule = lifeRule
        self.RowSize = nsize
        self.ColumnSize = msize
        self.Scale = scale
        self.dencity = dencity
        self.MyArray = array('H', (False for s in range(self.RowSize * self.ColumnSize)))
        self.init_life(dencity)
        self.canvas = Canvas(root, width=self.RowSize*self.Scale, height=self.ColumnSize*self.Scale, bg="black")
        self.canvas.pack()
        self.next_move()

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

    def draw_earth(self):

        for i in range(self.RowSize):
            for j in range(self.ColumnSize):
                color = 'black'
                if self.get(i, j):
                    color = 'yellow'
                self.canvas.create_oval(i * self.Scale, j * self.Scale, i * self.Scale + self.Scale,
                                 j * self.Scale + self.Scale, fill=color)
        self.canvas.update()

    def next_generation(self):
        for i in range(self.RowSize):
            for j in range(self.ColumnSize):
                alive = self.get(i, j)
                comfort_level = self.lifeRule.get_comfort_level(self.MyArray, self.RowSize, self.ColumnSize, i, j);
                if alive and comfort_level == IS_UNPLEASURE:
                    self.unset(i, j)
                if not alive and comfort_level == IS_PLEASURE:
                    self.set(i, j)

    def next_move(self):
        self.next_generation()
        self.draw_earth()
        self.canvas.after(100, self.next_move())
