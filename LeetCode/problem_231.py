# LEETCODE
# giraycoskun
# Problem 231: Power of Two
# Easy
# https://www.geeksforgeeks.org/python-program-to-find-whether-a-no-is-power-of-two/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and (not(n & (n - 1)))
    