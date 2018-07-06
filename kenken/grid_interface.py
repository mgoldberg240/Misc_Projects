# Sources: https://stackoverflow.com/questions/30023763/how-to-make-an-interactive-2d-grid-in-a-window-in-python
from tkinter import *

class Cell():
    FILLED_COLOR_BG = "light goldenrod"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "white"
    EMPTY_COLOR_BORDER = "black"

    def __init__(self, master, x, y, size):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill= False

    def _switch(self):
        """ Switch if the cell is filled or not. """
        self.fill= not self.fill
        xmin = self.abs * self.size
        xmax = xmin + self.size
        ymin = self.ord * self.size
        ymax = ymin + self.size

    # def confirm_mini(self):
    #     self.fill = EMPTY_COLOR_BG = "white"
    #     self.outline = FILLED_COLOR_BORDER = "white"

    def draw(self):
        """ order to the cell to draw its representation on the canvas """
        
        if self.master != None : # any user action
            fill = Cell.FILLED_COLOR_BG
            outline = Cell.FILLED_COLOR_BORDER
            w = 5
            text_on = 1


            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER
                w = 1
                text_on = 0
                # self.minis.append([abs,ord])

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            xmid = int((xmax-xmin)/2)
            ymid = int((ymax-ymin)/2)
            xmid = xmid + xmin
            ymid = ymid + ymin

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline,width = w)

            if text_on:
                self.master.create_text(xmid, ymid, fill = 'black',text = '%s,%s'%(xmid,ymid))


class CellGrid(Canvas,Menu):
    def __init__(self,master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Menu.__init__(self, master)
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)


        # self.win2 = Menu(self)
        # self.win2.pack(side="left", padx=100, pady=100)

        self.cellSize = cellSize

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))

            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []
        self.minis = []

        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)  
        #bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of midified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.draw()



    def record_minis(self,cell):
        cellindex = [cell.ord,cell.abs]
        if cellindex in self.minis:
            self.minis.remove(cellindex)
        else:
            self.minis.append(cellindex)
        print(self.minis)

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch()
        cell.draw()
        self.record_minis(cell)
        #add the cell to the list of cell switched during the click
        self.switched.append(cell)

    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch()
            cell.draw()
            self.record_minis(cell)
            self.switched.append(cell)


class Menu(Frame):
    def __init__(self,master,*args, **kwargs):

        Frame.__init__(self, *args, **kwargs)

        L = Label(master, text = "enter mini data",font=("Ariel", 16))
        L.pack(side="right",expand=True, padx=2, pady=2)


        entry = Entry(master)
        entry.pack(side="right",expand=True, padx=2, pady=2)
        entry.focus_set()


        def callback():
            text = entry.get()
            print(text)
            # cell.confirm_mini(self)

        button = Button(master,height = 4,width = 15, text = 'create mini', font=("Ariel", 16),command=callback)
        button.pack(side="right", expand=True, padx=2, pady=2)



if __name__ == "__main__" :
    n = int(input("Input size of puzzle: "))
    app = Tk()
    grid = CellGrid(app, n, n, 100)
    grid.pack()


    app.mainloop()
    # entry = Entry(master, width=50)
    # entry.pack()



# https://stackoverflow.com/questions/18171328/python-2-7-super-error
# https://stackoverflow.com/questions/26315848/how-to-count-the-number-of-times-a-button-is-clicked-pythontkinter



