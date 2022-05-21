# LEETCODE
# giraycoskun
# Problem 191: Number of 1 Bits
# Easy

def hammingWeight(n: int) -> int:
    n = str(bin(n))
    count = 0
    for c in n:
        if c == '1':
            count += 1
    return count


if __name__ == '__main__':
    test = hammingWeight(4)
    print(f"TEST 1: {test}")
