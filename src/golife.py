from src.Earth import Earth
from src.Moore import Moore

import tkinter



DENCITY = 2
VISUAL_SCALE = 5
ARRAY_SIZE_ROW = 20
ARRAY_SIZE_COLUMN = 20


if __name__ == "__main__":

    root = tkinter.Tk()

    earthRule = Moore()

    arr = Earth(ARRAY_SIZE_ROW, ARRAY_SIZE_COLUMN, VISUAL_SCALE, DENCITY, earthRule, root)
    root.mainloop()
