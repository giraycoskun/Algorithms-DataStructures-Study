# LEETCODE
# giraycoskun
# Problem 695: Max Area of Island
# Medium

def maxAreaOfIsland(grid: list[list[int]]) -> int:
    X = len(grid)
    Y = len(grid[0])
    max_area = 0
    for i in range(X):
        for j in range(Y):
            if grid[i][j] == 1:
                area = 0
                stack = [(i, j)]
                grid[i][j] = 0
                while len(stack) != 0:
                    x, y = stack.pop()
                    area += 1
                    if x + 1 < X:
                        if grid[x + 1][y] == 1:
                            grid[x+1][y] = 0
                            stack.append((x + 1, y))
                    if x - 1 >= 0:
                        if grid[x - 1][y] == 1:
                            grid[x-1][y] = 0
                            stack.append((x - 1, y))
                    if y + 1 < Y:
                        if grid[x][y + 1] == 1:
                            grid[x][y+1] = 0
                            stack.append((x, y + 1))
                    if y - 1 >= 0:
                        if grid[x][y - 1] == 1:
                            grid[x][y-1] = 0
                            stack.append((x, y - 1))
                if area > max_area:
                    max_area = area
    return max_area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    test = maxAreaOfIsland(grid)
    print(f"TEST 1: {test}")

    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    test = maxAreaOfIsland(grid)
    print(f"TEST 2: {test}")
