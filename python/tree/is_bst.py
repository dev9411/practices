class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def is_bst(self, low=float('-inf'), high=float('inf')):
        if not self:
            return True
        
        if not (low < self.value <= high):
            return False
        
        if not self.left and not self.right:
            return True
        
        if not self.left:
            return self.right.is_bst(self.value, high)
        
        if not self.right:
            return self.left.is_bst(low, self.value)
        
        return self.left.is_bst(low, self.value) and self.right.is_bst(self.value, high)
