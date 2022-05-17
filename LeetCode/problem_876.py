# LEETCODE
# giraycoskun
# Problem 876: Middle of the Linked List
# Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        hare = head

        while hare.next is not None:
            hare = hare.next
            tortoise = tortoise.next
            if hare.next is None:
                break
            else:
                hare = hare.next

        return tortoise
