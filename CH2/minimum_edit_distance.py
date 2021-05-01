import numpy as np

def min_edit_distance(source, target):
    n = len(source)
    m = len(target)
    D = np.zeros([n+1, m+1])

    for i in range(1, n+1):
        D[i][0] = D[i-1][0] + 1
    for j in range(1, m+1):
        D[0][j] = D[0][j-1] + 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = min(D[i-1][j] + 1, D[i-1][j-1] + 2, D[i][j-1] + 1)

    return D

min_edit_distance('intention', 'execution')
