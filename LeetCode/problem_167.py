# LEETCODE
# giraycoskun
# Problem 167: Two Sum II - Input Array Is Sorted
# Medium

def twoSum(numbers: list[int], target: int) -> list[int]:
    index = 0
    for _ in range(len(numbers)):
        num2 = target - numbers[index]

        high = len(numbers) - 1
        low = index + 1
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == num2:
                return [index + 1, mid + 1]
            elif numbers[mid] < num2:
                low = mid + 1
            else:
                high = mid - 1
        index += 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    test = twoSum(numbers, target)
    print(f"TEST 1: {test}")

    numbers = [2, 3, 4]
    target = 6
    test = twoSum(numbers, target)
    print(f"TEST 2: {test}")

    numbers = [-1, 0]
    target = -1
    test = twoSum(numbers, target)
    print(f"TEST 3: {test}")

    numbers = [5, 25, 75]
    target = 100
    test = twoSum(numbers, target)
    print(f"TEST 4: {test}")
