# LEETCODE
# giraycoskun
# Problem 2: Add Two Numbers
# Medium
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    value = ListNode()
    checksum = 0
    prev = value
    while l1 is not None or l2 is not None:
        if l1 is not None:
            l1_val = l1.val
            l1 = l1.next
        else:
            l1_val = 0
        if l2 is not None:
            l2_val = l2.val
            l2 = l2.next
        else:
            l2_val = 0

        new_node = ListNode()
        result = l1_val + l2_val + checksum
        checksum = 0
        if result > 9:
            checksum = 1
            result = result % 10
        new_node.val = result
        prev.next = new_node
        prev = new_node
    if checksum == 1:
        new_node = ListNode()
        new_node.val = 1
        prev.next = new_node
    return value.next


if __name__ == '__main__':
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    head1 = ListNode()
    head1.val = l1[0]
    head1.next = None
    prev_node = head1
    for num in l1[1:]:
        ln1 = ListNode()
        ln1.val = num
        prev_node.next = ln1
        prev_node = ln1
    head2 = ListNode()
    head2.val = l2[0]
    head2.next = None
    prev_node = head2
    for num in l2[1:]:
        ln2 = ListNode()
        ln2.val = num
        prev_node.next = ln2
        prev_node = ln2
    test = addTwoNumbers(head1, head2)
    answer = []
    while test is not None:
        answer.append(test.val)
        test = test.next
    print(f"TEST 1: {answer}")
