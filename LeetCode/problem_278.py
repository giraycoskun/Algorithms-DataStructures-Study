# LEETCODE
# giraycoskun
# Problem 278: First Bad Version
# Easy


def firstBadVersion(n: int) -> int:
    high = n
    low = 1
    check = False
    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            check = True
            high = mid - 1
        else:
            check = False
            low = mid + 1

    if check:
        return mid
    else:
        return mid + 1


def isBadVersion(n):
    test = [False, False, False, True, True]
    return test[n]


if __name__ == '__main__':

    firstBadVersion(5)
