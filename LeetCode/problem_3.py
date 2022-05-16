# LEETCODE
# giraycoskun
# Problem 3: Longest Substring Without Repeating Characters
# Medium

def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    j = 0
    char_dict = {}
    longest_substr = 0
    for char in s:
        if char in char_dict and char_dict[char] > 0:
            longest_substr = max((j-i), longest_substr)
            while s[i] != char:
                char_dict[s[i]] = 0
                i += 1
            i += 1
            j += 1
        else:
            j += 1
            char_dict[char] = 1
    longest_substr = max((j - i), longest_substr)
    return longest_substr


if __name__ == '__main__':
    s = "abcabcbb"
    test = lengthOfLongestSubstring(s)
    print(f"TEST 1: {test}")

    s = "bbbbb"
    test = lengthOfLongestSubstring(s)
    print(f"TEST 2: {test}")

    s = "pwwkew"
    test = lengthOfLongestSubstring(s)
    print(f"TEST 3: {test}")

    s = " "
    test = lengthOfLongestSubstring(s)
    print(f"TEST 4: {test}")

