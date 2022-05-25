# LEETCODE
# giraycoskun
# Problem 542: 01 Matrix
# Medium
# Dynamic Programming

from helper import *


def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    r = len(mat)
    c = len(mat[0])
    dist = createMatrix(r, c, r * c)
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                dist[i][j] = 0
            else:
                values = []
                if i + 1 < r:
                    values.append(dist[i + 1][j] + 1)
                if i - 1 >= 0:
                    values.append(dist[i - 1][j] + 1)
                if j + 1 < c:
                    values.append(dist[i][j + 1] + 1)
                if j - 1 >= 0:
                    values.append(dist[i][j - 1] + 1)
                values.append(dist[i][j])
                dist[i][j] = min(values)

    for i in range(r-1, -1, -1):
        for j in range(c-1, -1, -1):
            if mat[i][j] == 0:
                dist[i][j] = 0
            else:
                values = []
                if i + 1 < r:
                    values.append(dist[i + 1][j] + 1)
                if i - 1 >= 0:
                    values.append(dist[i - 1][j] + 1)
                if j + 1 < c:
                    values.append(dist[i][j + 1] + 1)
                if j - 1 >= 0:
                    values.append(dist[i][j - 1] + 1)
                values.append(dist[i][j])
                dist[i][j] = min(values)
    return dist


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1]]
    test = updateMatrix(mat)
    print(f"TEST 1: {test}")

    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    test = updateMatrix(mat)
    print(f"TEST 2: {test}")

    mat = [[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]
    test = updateMatrix(mat)
    print(f"TEST 3: {test}")

    mat = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
    test = updateMatrix(mat)
    print(f"TEST 4: {test}")

