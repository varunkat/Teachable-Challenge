grid = [(1, [1, 1]), (2, [1, 2]), (3, [1, 3]), (4, [1, 4]), (5, [1, 5]), (6, [2, 1]), (7, [2, 2]), (8, [2, 3]), (9, [2, 4]), (10, [2, 5]), (11, [3, 1]), (12,
[3, 2]), (13, [3, 3]), (14, [3, 4]), (15, [3, 5]), (16, [4, 1]), (17, [4, 2]), (18, [4, 3]), (19, [4, 4]), (20, [4, 5]), (21, [5, 1]), (22, [5, 2]), (23, [5, 3]), (24, [5, 4]), (25, [5, 5])]

neighbors = []

def patterns(x, y, m, type):
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

def neighborhood_nodes(x, y, i, m ,type):
    if x and y is not None and i is None:
        nodes = patterns(x,y,m,type)
    elif i is not None:
        for node in grid:
            if node[0] == i:
                x = node[1][0]
                y = node[1][1]
                nodes = patterns(x,y,m,type)
    else:
        nodes = 'Expected either (x,y) or i'
    return nodes


n_nodes = neighborhood_nodes(x = None , y = 3, i = 13, m = 2, type = "CROSS")
print(n_nodes)
