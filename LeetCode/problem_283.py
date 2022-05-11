# LEETCODE
# giraycoskun
# Problem 283: Move Zeroes
# Easy

def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    index = 0
    length = len(nums)
    for _ in range(length):
        if nums[index] == 0:
            nums.pop(index)
            nums.append(0)
            index -= 1
        index += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(f"TEST 1: {nums}")

    nums =[0]
    moveZeroes(nums)
    print(f"TEST 2: {nums}")
