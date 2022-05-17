# LEETCODE
# giraycoskun
# Problem 19: Remove Nth Node From End of List
# Medium
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    current = head
    later = head
    for _ in range(n):
        later = later.next

    if later is None:
        return head.next

    while later.next is not None:
        later = later.next
        current = current.next

    current.next = current.next.next
    return head


if __name__ == '__main__':
    head = [1,2,3,4,5]
    n = 2
    new = ListNode()
    current = new
    current.val = head[0]
    for num in head[1:]:
        temp = ListNode()
        temp.val = num
        current.next = temp
        current = temp

    test = removeNthFromEnd(new, n)
    answer = []
    while test is not None:
        answer.append(test.val)
        test = test.next
    print(f"TEST 1: {answer}")

