# LEETCODE
# giraycoskun
# Problem 190: Reverse Bits
# Easy

def reverseBits(n: int) -> int:
    n = bin(n)
    n = n[-1:1:-1]
    n = n + (32 - len(n)) * '0'
    return int(n, 2)


if __name__ == '__main__':
    test = reverseBits(12)
