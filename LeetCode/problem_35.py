# LEETCODE
# giraycoskun
# Problem 35: Search Insert Position
# Easy


def searchInsert(nums: list[int], target: int) -> int:
    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    mid = (low + high) // 2
    return mid + 1


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    test = searchInsert(nums, target)
    print(f"TEST 1: {test}")

    nums = [1, 3, 5, 6]
    target = 2
    test = searchInsert(nums, target)
    print(f"TEST 2: {test}")

    nums = [1, 3, 5, 6]
    target = 7
    test = searchInsert(nums, target)
    print(f"TEST 3: {test}")

    nums = [1, 3, 5, 6]
    target = 0
    test = searchInsert(nums, target)
    print(f"TEST 4: {test}")
