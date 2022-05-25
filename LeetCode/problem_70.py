# LEETCODE
# giraycoskun
# Problem 70: Climbing Stairs
# Easy
# Recursion
# Dynamic (memoization)

def climbStairs(n: int) -> int:
    def solve(n):
        if n <= 1:
            return 1

        if dp[n] != -1:
            return dp[n]

        dp[n] = solve(n-1) + solve(n-2)
        return dp[n]

    dp = [-1]*(n+1)
    return solve(n)


if __name__ == '__main__':
    test = climbStairs(4)