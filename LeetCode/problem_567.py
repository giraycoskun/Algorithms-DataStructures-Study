# LEETCODE
# giraycoskun
# Problem 567: Permutation in String
# Medium

def checkInclusion(s1: str, s2: str) -> bool:
    d = {}
    for c in s1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    i = 0
    j = 0
    for idx in range(len(s2)):
        if s2[idx] in d and d[s2[idx]] > 0:
            j +=1
            d[s2[idx]] -= 1
        else:
            i += 1
            while i < idx:
                d[s2[i]] += 1
                i += 1
            i += 1
            j -= 1
        if (j-i) == len(s1):
            return True
    return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    test = checkInclusion(s1, s2)
    print(f"TEST 1: {test}")

    s1 = "ab"
    s2 = "eidboaoo"
    test = checkInclusion(s1, s2)
    print(f"TEST 2: {test}")

    s1 = "ab"
    s2 = "ab"
    test = checkInclusion(s1, s2)
    print(f"TEST 3: {test}")

    s1 = "hello"
    s2 = "ooolleoooleh"
    test = checkInclusion(s1, s2)
    print(f"TEST 4: {test}")

    s1 = "adc"
    s2 = "dcda"
    test = checkInclusion(s1, s2)
    print(f"TEST 5: {test}")