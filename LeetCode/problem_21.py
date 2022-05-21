# LEETCODE
# giraycoskun
# Problem 21: Merge Two Sorted Lists
# Easy
# Recursion

from typing import Optional
from helper import *


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val > list2.val:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
    else:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1


if __name__ == '__main__':
    l1 = [1, 2]
    l2 = [1, 3]
    l1 = arrayToList(l1)
    l2 = arrayToList(l2)
    test = mergeTwoLists(l1, l2)
    display(test)
