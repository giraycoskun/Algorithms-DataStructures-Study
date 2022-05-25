# LEETCODE
# giraycoskun
# Problem 77: Combinations
# Medium
# Recursion

def combine(n: int, k: int) -> list[list[int]]:
    def solve(n, i, l):
        if i == 0:
            result = []
            for item in temp:
                result.append(item)
            ans.append(result)
            return

        for j in range(l, n+1):
            temp.append(j)
            solve(n, i-1, j+1)
            temp.pop()
        return

    ans = []
    temp = []
    solve(n, k, 1)
    return ans


if __name__ == '__main__':
    test = combine(4, 2)
    print(f"Test 1: {test}")
