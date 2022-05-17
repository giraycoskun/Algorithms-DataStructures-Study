# LEETCODE
# giraycoskun
# Problem 733: Flood Fill
# Easy

def floodFill(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    # BREADTH-FIRST
    vertical_boundary = len(image)
    horizontal_boundary = len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image
    stack = [(sr, sc)]
    while len(stack) > 0:
        sr, sc = stack.pop()
        if sr + 1 < vertical_boundary:
            if image[sr + 1][sc] == color:
                stack.append((sr + 1, sc))
        if sr - 1 >= 0:
            if image[sr - 1][sc] == color:
                stack.append((sr - 1, sc))
        if sc + 1 < horizontal_boundary:
            if image[sr][sc + 1] == color:
                stack.append((sr, sc + 1))
        if sc - 1 >= 0:
            if image[sr][sc - 1] == color:
                stack.append((sr, sc - 1))
        image[sr][sc] = newColor
    return image


if __name__ == '__main__':
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    test = floodFill(image, sr, sc, newColor)
    print(f"TEST 1: {test}")

    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    test = floodFill(image, sr, sc, newColor)
    print(f"TEST 1: {test}")
