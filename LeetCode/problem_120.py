# LEETCODE
# giraycoskun
# Problem 120: Triangle
# Medium
# Dynamic Programming without Recursion Bottom-Up Approach

def minimumTotal(triangle: list[list[int]]) -> int:
    memory = [0] * len(triangle[-1])

    for i in range(len(triangle[-1])):
        memory[i] = triangle[-1][i]

    for i in range(len(triangle)-2, -1, -1):
        for j in range(i+1):
            memory[j] = min(memory[j], memory[j+1]) + triangle[i][j]

    return memory[0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    test = minimumTotal(triangle)
