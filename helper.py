# Definition for a Node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None, next: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion
    if i < n:
        root = TreeNode(arr[i])

        # insert left child
        root.left = insertLevelOrder(arr, 2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, 2 * i + 2, n)

    return root


def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


# Function to insert node
def insert(root, item):
    temp = ListNode(item)
    if root is None:
        root = temp
    else:
        ptr = root
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = temp
    return root


def display(root):
    while root is not None:
        print(root.val, end=" ")
        root = root.next


def arrayToList(arr):
    root = None
    for i in range(0, len(arr), 1):
        root = insert(root, arr[i])
    return root


def createMatrix(row, col, val):
    return [[val for _ in range(col)] for _ in range(row)]
