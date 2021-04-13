test = [(1, [1, 1]), (2, [1, 2]), (3, [1, 3]), (4, [1, 4]), (5, [1, 5]), (6, [2, 1]), (7, [2, 2]), (8, [2, 3]), (9, [2, 4]), (10, [2, 5]), (11, [3, 1]), (12,
[3, 2]), (13, [3, 3]), (14, [3, 4]), (15, [3, 5]), (16, [4, 1]), (17, [4, 2]), (18, [4, 3]), (19, [4, 4]), (20, [4, 5]), (21, [5, 1]), (22, [5, 2]), (23, [5, 3]), (24, [5, 4]), (25, [5, 5])]

neighbors = []
#-----------------------CROSS---------------------------------------
x = 3
y = 3
m = 2
count = 0
tot1 = y+m
tot2 = x+m
T = (x,y)
neighbors.append(T)
for i in test:
    for v in range(0, m + 1):
        if i[1][0] == x and i[1][1] == y:
            continue

        if i[1][0] == x - v:
            for j in range(y - m + v, tot1 + 1 - v):
                if i[1][1] == j:
                    T = (x - v, j)
                    if T in neighbors:
                        continue
                    else:
                        neighbors.append(T)

        if i[1][0] == x + v:
            for j in range(y - m + v, tot1 + 1 - v):
                if i[1][1] == j:
                    T = (x + v, j)
                    if T in neighbors:
                        continue
                    else:
                        neighbors.append(T)

    '''if i[1][1] == y:
        for k in range(x-m, tot2+1):
            if i[1][0] == k:
                T1 = (k, y)
                neighbors.append(T1)'''

















'''for i in test:
    if i[1][0] == x and i[1][1] == y:
        continue
    if i[1][0] == x:
        for j in range(y-m, tot1+1):
            if i[1][1] == j:
                T = (x, j)
                neighbors.append(T)

    if i[1][1] == y:
        for k in range(x-m, tot2+1):
            if i[1][0] == k:
                T1 = (k, y)
                neighbors.append(T1)'''

#------------------------SQUARE-----------------------------------------
'''for cord in test:
    for i in range(x-m, x + m + 1):
        for j in range(y-m, y + m + 1):
            if cord[1][0] == i and cord[1][1] == j:
                T = (i,j)
                neighbors.append(T)'''




print(neighbors)
