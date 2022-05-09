# 977. Squares of a Sorted Array
# easy


def sorted_squares(nums):
    mini = 0
    maxi = len(nums) - 1
    sorted_square_list = []
    while mini != maxi:
        if abs(nums[mini]) <= abs(nums[maxi]):
            num = nums[maxi] * nums[maxi]
            maxi -= 1
        else:
            num = nums[mini] * nums[mini]
            mini += 1
        sorted_square_list.insert(0, num)
    num = nums[mini] * nums[mini]
    sorted_square_list.insert(0, num)
    print(sorted_square_list)
    return sorted_square_list


if __name__ == '__main__':
    test1 = [-7, -3, 2, 3, 11]

    sorted_squares(test1)
