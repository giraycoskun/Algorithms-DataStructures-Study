# LEETCODE
# giraycoskun
# Problem 1: Two Sum
# Easy


def twoSum(nums: list[int], target: int) -> list[int]:
    data = {}
    length = len(nums)
    for k in range(length):
        diff = target - nums[k]
        if nums[k] in data:
            return [k, data[nums[k]]]
        else:
            data[diff] = k