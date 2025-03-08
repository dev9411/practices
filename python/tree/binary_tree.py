from typing import Optional

class TreeNode:
    def __init__(self, data: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.data = data
        self.right = right
        self.left = left

def visit(node: TreeNode):
    print(node.data)
        
def inOrderTraversal(node: TreeNode):
    if node is None:
        return
    
    inOrderTraversal(node.left)
    visit(node)
    inOrderTraversal(node.right)
        
def preOrderTraversal(node: TreeNode):
    if node is None:
        return

    visit(node)    
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def postOrderTraversal(node: TreeNode):
    if node is None:
        return

    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    visit(node)    
