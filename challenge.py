import numpy as np

grid = []

class NeighboringNodes():

    def __init__(self, size, debug):
        self.size = int(size)
        self.debug = debug

    def create_grid(self):
        grid1 = [[row,col] for row in range(self.size) for col in range(self.size)]

        for i in enumerate(grid1, 1):
            grid.append(i)

        if self.debug == 'True' or self.debug == 'true':
            for i in grid:
                feature = (i[1][0], i[1][1], i[0])
                print(feature)

        #grid= np.zeros((self.size, self.size))
        #return grid

    def return_cords(self, index):
        self.index= index
        for i in grid:
            if i[0] == index:
                T = (i[1][0], i[1][1])
        return T

obj = NeighboringNodes(3,'false')
obj.create_grid()
cords = obj.return_cords(3)
print(cords)
