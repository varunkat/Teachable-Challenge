
grid = []
neighbors = []

class NeighboringNodes():

    def __init__(self, size, debug:bool):
        self.size = int(size)
        self.debug = debug


    def create_grid(self):
        grid1 = [[row,col] for row in range(1, self.size + 1) for col in range(1, self.size + 1)]

        for i in enumerate(grid1, 1):
            grid.append(i)
        #print(grid)

        if self.debug == True:
            for node in grid:
                feature = (node[1][0], node[1][1], node[0])
                print(feature)


    def return_cords(self, index):
        for node in grid:
            if node[0] == index:
                T = (node[1][0], node[1][1])
        return T
#------------------------END OF TASK 1-----------------------------------------
    def patterns(self, x, y, i, m, type):
        if x is not None and y is not None and i is not None:
            print("expected either x & y or i")
        else:
            T = (x,y)
            neighbors.append(T)
            for node in grid:
                if type == "CROSS":
                    if node[1][0] == x and node[1][1] == y:
                        continue
                    if node[1][0] == x:
                        for j in range(y - m, y + m + 1):
                            if node[1][1] == j:
                                T = (x, j)
                                neighbors.append(T)

                    if node[1][1] == y:
                        for k in range(x - m, x + m + 1):
                            if node[1][0] == k:
                                T1 = (k, y)
                                neighbors.append(T1)

                elif type == "SQUARE":
                    for i in range(x - m, x + m + 1):
                        for j in range(y - m, y + m + 1):
                            if node[1][0] == x and node[1][1] == y:
                                continue
                            if node[1][0] == i and node[1][1] == j:
                                T = (i,j)
                                neighbors.append(T)

                elif type == "DIAMOND":
                    for v in range(0, m + 1):
                        if node[1][0] == x and node[1][1] == y:
                            continue

                        if node[1][0] == x - v:
                            for j in range(y - m + v, y + m + 1 - v):
                                if node[1][1] == j:
                                    T = (x - v, j)
                                    if T in neighbors:
                                        continue
                                    else:
                                        neighbors.append(T)

                        if node[1][0] == x + v:
                            for j in range(y - m + v, y + m + 1 - v):
                                if node[1][1] == j:
                                    T = (x + v, j)
                                    if T in neighbors:
                                        continue
                                    else:
                                        neighbors.append(T)

        return neighbors

object = NeighboringNodes(5, False)
object.create_grid()
cords = object.return_cords(12)
neighbor_nodes = object.patterns(x = 3, y = 3, i = None , m = 2, type = "DIAMOND")
print(cords)
print(neighbor_nodes)
