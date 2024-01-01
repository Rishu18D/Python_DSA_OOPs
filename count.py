class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_common_ancestor(root, node1, node2):
    if not root:
        return None

    if root.val == node1 or root.val == node2:
        return root

    left_ancestor = find_common_ancestor(root.left, node1, node2)
    right_ancestor = find_common_ancestor(root.right, node1, node2)

    if left_ancestor and right_ancestor:
        return root

    return left_ancestor if left_ancestor else right_ancestor
