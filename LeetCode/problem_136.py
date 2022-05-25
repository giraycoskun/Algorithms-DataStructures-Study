# LEETCODE
# giraycoskun
# Problem 136: Single Number
# Easy

def singleNumber(nums: list[int]) -> int:
    answer = 0
    for num in nums:
        answer = answer ^ num
    return answer
