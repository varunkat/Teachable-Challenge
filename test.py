test = [(1, [1, 1]), (2, [1, 2]), (3, [1, 3]), (4, [1, 4]), (5, [2, 1]), (6, [2, 2]), (7, [2, 3]), (8, [2, 4]), (9, [3, 1]), (10, [3, 2]), (11, [3, 3]), (12,
[3, 4]), (13, [4, 1]), (14, [4, 2]), (15, [4, 3]), (16, [4, 4])]

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
'''for i in test:
    if i[1][0] == x and i[1][1] == y:
        continue
    if i[1][0] == x:
        for j in range(1, tot1+1):
            if i[1][1] == j:
                T = (x, j)
                neighbors.append(T)

    if i[1][1] == y:
        for k in range(1, tot2+1):
            if i[1][0] == k:
                T1 = (k, y)
                neighbors.append(T1)'''

#------------------------SQUARE-----------------------------------------
for cord in test:
    for i in range(x-m, x + m + 1):
        for j in range(y-m, y + m + 1):
            if cord[1][0] == i and cord[1][1] == j:
                T = (i,j)
                neighbors.append(T)




print(neighbors)
