# LEETCODE
# giraycoskun
# Problem 557: Reverse Words in a String III
# Easy

def reverseWords(s: str) -> str:
    words = s.split()
    for k in range(len(words)):
        words[k] = words[k][::-1]
    return ' '.join(words)


if __name__ == '__main__':
    s = "Let's tak e LeetCode contest"
    test = reverseWords(s)
    print(f"TEST 1: {test}")

    s = "God Ding"
    test = reverseWords(s)
    print(f"TEST 2: {test}")
