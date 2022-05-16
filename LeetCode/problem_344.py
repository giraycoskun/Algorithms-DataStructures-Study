# LEETCODE
# giraycoskun
# Problem 344: Reverse String
# Easy

def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    high = len(s) - 1
    low = 0
    while low < high:
        temp = s[low]
        s[low] = s[high]
        s[high] = temp
        high -= 1
        low += 1


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(f"TEST 1: {s}")

    s = ["H", "a", "n", "n", "a", "h"]
    reverseString(s)
    print(f"TEST 2: {s}")
