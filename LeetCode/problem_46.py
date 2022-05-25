# LEETCODE
# giraycoskun
# Problem 46: Permutations
# Medium
# Recursion

def permute(nums: list[int]) -> list[list[int]]:
    def solve(nums, i):
        if i == 0:
            return [[]]
        ans = []
        for n in range(len(nums)):
            temp = nums[:n] + nums[n+1:]
            results = solve(temp, i-1)
            for result in results:
                result.append(nums[n])
                ans.append(result)
        return ans

    return solve(nums, len(nums))


if __name__ == '__main__':
    nums = [1, 2, 3]
    test = permute(nums)
    print(f"Test 1: {test}")
