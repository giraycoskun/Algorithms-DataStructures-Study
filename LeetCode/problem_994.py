# LEETCODE
# giraycoskun
# Problem 994: Rotting Oranges
# Medium
# Dynamic Programming

from helper import *


def orangesRotting(grid: list[list[int]]) -> int:
    r = len(grid)
    c = len(grid[0])
    rotten_queue = []
    oranges = set()
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                rotten_queue.append((i, j))
            if grid[i][j] == 1:
                oranges.add((i, j))

    if len(oranges) == 0:
        return 0

    level = 0
    while len(rotten_queue) != 0:
        level_size = len(rotten_queue)
        while level_size != 0:
            level_size -= 1
            i, j = rotten_queue.pop(0)
            if i + 1 < r:
                item = (i + 1, j)
                if item in oranges:
                    rotten_queue.append(item)
                    oranges.discard(item)
            if i - 1 >= 0:
                item = (i - 1, j)
                if item in oranges:
                    rotten_queue.append(item)
                    oranges.discard(item)

            if j + 1 < c:
                item = (i, j + 1)
                if item in oranges:
                    rotten_queue.append(item)
                    oranges.discard(item)

            if j - 1 >= 0:
                item = (i, j - 1)
                if item in oranges:
                    rotten_queue.append(item)
                    oranges.discard(item)
        level += 1

    if len(oranges) != 0:
        return -1
    else:
        return level-1


if __name__ == '__main__':
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    test = orangesRotting(grid)
    print(f"TEST 1: {test}")

    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    test = orangesRotting(grid)
    print(f"TEST 2: {test}")
