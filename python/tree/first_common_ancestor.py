# First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
# Hints: #70, #76, #28, #36, #46, #70, #80, #96

class Node:
    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right

def first_common_ancestor(root: Node, value1: int, value2: int):
    if root is None:
        return None

    if root.value == value1 or root.value == value2:
        return root

    left = first_common_ancestor(root.left, value1, value2)
    right = first_common_ancestor(root.right, value1, value2)

    if left and right:
        return root

    return left or right