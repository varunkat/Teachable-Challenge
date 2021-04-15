
grid = []   # empty list for creating grid (Task1)
neighbors = []   #empty list for capturing nodes for different patterns (Task 2)

class NeighboringNodes():  # initiating main class

    def __init__(self, size, debug:bool): #passing parameters to class
        self.size = int(size)
        self.debug = debug

    def create_grid(self): # method to create grid
        grid1 = [[row,col] for row in range(1, self.size + 1) for col in range(1, self.size + 1)] #assigning coordinates to nodes

        for i in enumerate(grid1, 1): #assigning index value of the order of node creation
            grid.append(i)
        #print(grid)

        if self.debug == True: #printing (x,y,i) parameters for all nodes in grid
            for node in grid:
                feature = (node[1][0], node[1][1], node[0])
                print(feature)


    def return_cords(self, index): # method to return (x,y) coordinates for specified node index value
        try:
            for node in grid:
                if node[0] == index:
                    T = (node[1][0], node[1][1])
            return T
        except:
            print('Index value is out of range, enter correct value')

#----------------------------------------END OF TASK 1-------------------------------------------------------------

    def patterns(self, x, y, m, type): # method to process neighbor nodes based on provided pattern
        T = (x,y)
        neighbors.append(T) #appending given root node from where neighbors has to be discovered
        for node in grid:
            if type == "CROSS": # code block for CROSS pattern
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

            elif type == "SQUARE": # code block for SQUARE pattern
                for i in range(x - m, x + m + 1):
                    for j in range(y - m, y + m + 1):
                        if node[1][0] == x and node[1][1] == y:
                            continue
                        if node[1][0] == i and node[1][1] == j:
                            T = (i,j)
                            neighbors.append(T)

            elif type == "DIAMOND": # code block for DIAMOND pattern
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

    def neighborhood_nodes(self, x, y, i, m ,type): #method to return neighborhood nodes based on pattern provided
        if m > 0 and m <= self.size/2:  #checking if radius is in range
            if x and y is not None and i is None: # code block to accept either (x,y) or index value
                nodes = self.patterns(x,y,m,type)
            elif i is not None:
                for node in grid:
                    if node[0] == i:
                        x = node[1][0]
                        y = node[1][1]
                        nodes = self.patterns(x,y,m,type)
            else:
                nodes = 'Expected either (x,y) or i' # error message when wrong parameters are provided
        else:
            nodes = 'Radius is out of range' # error message for radius
        return nodes
#----------------------------------------END OF TASK 2----------------------------------------------------------------------

#---------------------------------------PASSING PARAMETETERS BASED ON USER REQUIREMENTS-------------------------------------
object = NeighboringNodes(7, False)
object.create_grid()
coordinates = object.return_cords(12)
neighbor_nodes = object.neighborhood_nodes(x = 4, y = 4, i = None , m = 2, type = "DIAMOND") 
print(coordinates)
print(neighbor_nodes)
