from src.Earth import Earth
from src.Moore import Moore
import tkinter
from datetime import datetime


DENCITY = 2
VISUAL_SCALE = 7
ARRAY_SIZE_ROW = 20
ARRAY_SIZE_COLUMN = 20


def drawEarth():

    for i in range(ARRAY_SIZE_ROW):
        for j in range(ARRAY_SIZE_COLUMN):
            color = 'black'
            if arr.get(i, j):
                color = 'yellow'
            canv.create_oval(i * VISUAL_SCALE, j * VISUAL_SCALE, i * VISUAL_SCALE + VISUAL_SCALE, j * VISUAL_SCALE + VISUAL_SCALE, fill = color)
    canv.update()


if __name__ == "__main__":

    root = tkinter.Tk()
    canv = tkinter.Canvas(root, width=ARRAY_SIZE_ROW*VISUAL_SCALE, height=ARRAY_SIZE_COLUMN*VISUAL_SCALE, bg="black")
    canv.pack()

    earthRule = Moore()

    arr = Earth(ARRAY_SIZE_ROW, ARRAY_SIZE_COLUMN, earthRule)
    arr.init_life(DENCITY)

    while True:
        start_time = datetime.now()
        arr.next_generation()
        delta_1 = datetime.now() - start_time

        start_time = datetime.now()
        drawEarth()
        delta_2 = datetime.now() - start_time
        print('delta Generate: ', delta_1, '\t delta Canvas: ', delta_2)
