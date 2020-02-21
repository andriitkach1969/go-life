import sys

from src.Earth import Earth
from src.Moore import Moore

import tkinter



DENCITY = 5
VISUAL_SCALE = 10
ARRAY_SIZE_ROW = 10
ARRAY_SIZE_COLUMN = 10


if __name__ == "__main__":

    root = tkinter.Tk()

    earthRule = Moore()
    arr = Earth(ARRAY_SIZE_ROW, ARRAY_SIZE_COLUMN, VISUAL_SCALE, DENCITY, earthRule, root)

    root.bind("<KeyPress-Left>", lambda e: sys.exit(0))
    root.mainloop()
