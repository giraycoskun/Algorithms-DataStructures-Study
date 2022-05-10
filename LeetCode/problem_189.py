# LEETCODE
# giraycoskun
# Problem 189: Rotate Array
# Medium

def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for _ in range(k):
        num = nums.pop()
        nums.insert(0, num)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print(f"TEST 1: {nums}")

    nums = [-1, -100, 3, 99]
    k = 2
    rotate(nums, k)
    print(f"TEST 2: {nums}")