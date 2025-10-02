class TreeNode(object):
    def __init__(
        self, 
        value: int, 
        left: 'TreeNode' | None = None, 
        right: 'TreeNode' | None = None, 
        parent: 'TreeNode' | None = None
    ):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
    def is_right_child(self):
        if self.parent is None:
            return False
        return self.parent.right == self
    
    def is_left_child(self):
        if self.parent is None:
            return False
        return self.parent.left == self

def get_first_inorder_node(root: TreeNode):
    if root.left is None:
        return root
    return get_first_inorder_node(root.left)

def get_next_in_order_parent(node: TreeNode):
    if node.parent is None:
        return None
    if node.parent.is_left_child():
        return node.parent.parent
    return get_next_in_order_parent(node.parent)
    
def get_in_order_successor(node: TreeNode):
    if node.right is not None:
        return get_first_inorder_node(node.right)
    if node.is_right_child():
        return get_next_in_order_parent(node)
    return node.parent
