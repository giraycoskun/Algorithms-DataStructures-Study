# LEETCODE
# giraycoskun
# Problem 567: Permutation in String
# Medium
# Sliding Window and HashMap

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    s1_map = [0]*26
    s2_map = [0]*26
    for i in range(len(s1)):
        num1 = ord(s1[i]) - ord('a')
        num2 = ord(s2[i]) - ord('a')
        s1_map[num1] += 1
        s2_map[num2] += 1

    for i in range(len(s1), len(s2)):
        if s1_map == s2_map:
            return True
        num1 = ord(s2[i]) - ord('a')
        num2 = ord(s2[i-len(s1)]) - ord('a')
        s2_map[num1] += 1
        s2_map[num2] -= 1

    return s1_map == s2_map


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    test = checkInclusion(s1, s2)
    print(f"TEST 1: {test}")  # TRUE

    s1 = "ab"
    s2 = "eidboaoo"
    test = checkInclusion(s1, s2)
    print(f"TEST 2: {test}")  # FALSE

    s1 = "ab"
    s2 = "ab"
    test = checkInclusion(s1, s2)
    print(f"TEST 3: {test}")

    s1 = "hello"
    s2 = "ooolleoooleh"
    test = checkInclusion(s1, s2)
    print(f"TEST 4: {test}")  # FALSE

    s1 = "adc"
    s2 = "dcda"
    test = checkInclusion(s1, s2)
    print(f"TEST 5: {test}")  # TRUE