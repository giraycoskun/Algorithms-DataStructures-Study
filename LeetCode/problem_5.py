# LEETCODE
# Problem 5: Longest Palindromic Substring
# Medium
# Dynamic Programming

"""
def longestPalindrome(s: str) -> str:

    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]

    dp = [[False for _ in range(len(s))] for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = True

    max_length = 1
    max_str = s[0]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = (s[i] == s[i+1])
            if max_length == 1:
                max_length = 2
                max_str = s[i] + s[i+1]


    #substring length
    for k in range(3, len(s)+1):
        #starting index
        for i in range(0, len(s)-k+1):
            j = i + k - 1

            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                if k > max_length:
                    max_length = k
                    max_str = s[i:j+1]
    return max_str
"""


def expandAroundCenter(s, i, j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return j - i - 1


def longestPalindrome(s):
    if len(s) < 1:
        return ""
    end = 0
    start = 0
    for i in range(len(s)):
        l1 = expandAroundCenter(s, i, i)
        l2 = expandAroundCenter(s, i, i+1)
        l = max(l1, l2)
        if l > (end - start):
            start = i - (l - 1) // 2
            end = i + l // 2
    return s[start:end+1]


if __name__ == '__main__':
    s = "babad"
    test = longestPalindrome(s)
    print(f"Test 1: {test}")

    s = "cbbd"
    test = longestPalindrome(s)
    print(f"Test 2: {test}")

    s = "a"
    test = longestPalindrome(s)
    print(f"Test 3: {test}")
