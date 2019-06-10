from src.libs import Earth
import tkinter


DENCITY = 5
VISUAL_SCALE = 10
ARRAY_SIZE_ROW = 20
ARRAY_SIZE_COLUMN = 20


if __name__ == "__main__":

    root = tkinter.Tk()
    canv = tkinter.Canvas(root, width=ARRAY_SIZE_ROW*VISUAL_SCALE, height=ARRAY_SIZE_COLUMN*VISUAL_SCALE, bg="black")
    canv.pack()

    arr = Earth(ARRAY_SIZE_ROW, ARRAY_SIZE_COLUMN)
    arr.init_life(DENCITY)

    try:
        while True:
            arr.next_generation()
            for i in range(ARRAY_SIZE_ROW):
                for j in range(ARRAY_SIZE_COLUMN):
                    if arr.get(i, j):
                        canv.create_oval(i * VISUAL_SCALE, j * VISUAL_SCALE, i * VISUAL_SCALE + VISUAL_SCALE, j * VISUAL_SCALE + VISUAL_SCALE, fill='yellow')
                    else:
                        canv.create_oval(i * VISUAL_SCALE, j * VISUAL_SCALE, i * VISUAL_SCALE + VISUAL_SCALE, j * VISUAL_SCALE + VISUAL_SCALE, fill='black')
            canv.update()

    except KeyboardInterrupt:
        pass
