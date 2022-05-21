# LEETCODE
# giraycoskun
# Problem 116: Populating Next Right Pointers in Each Node
# Medium

from typing import Optional

from helper import *


def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    if root is None:
        return root
    queue = [root]
    right = None
    level = 0
    count = 0
    while len(queue) != 0:
        if count == 2 ** level:
            level += 1
            right = None
            count = 0
        node = queue.pop(0)
        node.next = right
        right = node
        count += 1
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)
    return root


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7]
    root = insertLevelOrder(test, 0, len(test))
    root = connect(root)
    inOrder(root)
