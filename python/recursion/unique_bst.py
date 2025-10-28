# Given an integer n, return all the structurally unique BST's (binary search trees), 
# which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Example 1:
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# Example 2:
# Input: n = 1
# Output: [[1]]

from functools import lru_cache
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n: int):
    if n == 0:
        return []
    
    @lru_cache(None)
    def build(start, end):
        if start > end:
            return [None]
        all_trees = []
        for root_val in range(start, end + 1):
            for left in build(start, root_val - 1):
                for right in build(root_val + 1, end):
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    all_trees.append(root)
        return all_trees

    def serializeTree(trees: List[TreeNode]) -> List[List]:
        results = []
        for root in trees:
            results.append(convertToArray(root, []))
        return results

    def convertToArray(node: Optional[TreeNode], output: List) -> Optional[list]:
        if node is None:
            output.append(None)
            return
        output.append(node.val)
        if not node.left and not node.right:
            return output
        convertToArray(node.left, output)
        if not node.right and not node.left.left and not node.left.right:
            return output
        convertToArray(node.right, output)
        return output

    return serializeTree(build(1, n))

print(generateTrees(0))
print(generateTrees(1))
print(generateTrees(2))
print(generateTrees(3))
