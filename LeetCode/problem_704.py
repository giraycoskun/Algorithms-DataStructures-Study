# LEETCODE
# giraycoskun
# Problem 704: Binary Search
# Easy

def search(nums: list[int], target: int) -> int:
    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2  # rounds-down
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1


if __name__ == '__main__':
    test1 = [-1, 0, 3, 5, 9, 12]
    test1_target = 4
    test = search(test1, test1_target)
    print(f"TEST 1: {test}")
