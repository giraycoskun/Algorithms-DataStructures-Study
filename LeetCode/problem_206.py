# LEETCODE
# giraycoskun
# Problem 206: Reverse Linked List
# Easy
# Recursion

from typing import Optional
from helper import *


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    else:
        root = reverseList(head.next)
        head.next.next = head
        head.next = None
        return root


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    head = arrayToList(head)
    head = reverseList(head)
    display(head)
