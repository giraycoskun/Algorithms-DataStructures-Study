# LEETCODE
# giraycoskun
# Problem 784: Letter Case Permutation
# Medium


def letterCasePermutation(s: str) -> list[str]:
    if len(s) == 0:
        return []

    answer = [""]
    for c in s:
        if c.isalpha():
            for i in range(len(answer)):
                item = answer[i]
                answer[i] += c
                if c.isupper():
                    new_item = item + c.lower()
                else:
                    new_item = item + c.upper()
                answer.append(new_item)
        else:
            for i in range(len(answer)):
                answer[i] += c
    return answer


if __name__ == '__main__':
    s = "a1b2"
    test = letterCasePermutation(s)
    print(f"Test 1: {test}")

    s = "3z4"
    test = letterCasePermutation(s)
    print(f"Test 2: {test}")
