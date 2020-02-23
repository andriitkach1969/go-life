import sys

from src.Earth import Earth
from src.Moore import Moore
from src.neumann import Neumann

import tkinter


DENCITY = 10
VISUAL_SCALE = 10
ARRAY_SIZE_ROW = 50
ARRAY_SIZE_COLUMN = 50


if __name__ == "__main__":

    root = tkinter.Tk()

    rule_type = input('select neighbors. Moore - press 1 (default), Neumann - press 2:  ')
    earthRule = Neumann() if rule_type == 2 else Moore()
    arr = Earth(ARRAY_SIZE_ROW, ARRAY_SIZE_COLUMN, VISUAL_SCALE, DENCITY, earthRule.get_comfort_level, root)

    root.bind("<KeyPress-Left>", lambda e: sys.exit(0))
    root.bind("<KeyPress-Up>", lambda e: arr.delay_increase())
    root.bind("<KeyPress-Down>", lambda e: arr.delay_decrease())

    arr.next_move()
    root.mainloop()
