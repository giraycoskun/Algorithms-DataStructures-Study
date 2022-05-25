# LEETCODE
# giraycoskun
# Problem 198: House Robber
# Medium

def rob(nums: list[int]) -> int:
    current_max = 0
    prev_max = 0

    for num in nums:
        res = max(num + prev_max, current_max)
        prev_max = current_max
        current_max = res
    return current_max
