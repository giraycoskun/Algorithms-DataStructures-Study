# LEETCODE
# giraycoskun
# Problem 994: Rotting Oranges
# Medium
# Dynamic Programming

from helper import *


def orangesRotting(grid: list[list[int]]) -> int:
    r = len(grid)
    c = len(grid[0])
    max_time = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                queue = []
                while


if __name__ == '__main__':
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    test = orangesRotting(grid)
    print(f"TEST 1: {test}")
