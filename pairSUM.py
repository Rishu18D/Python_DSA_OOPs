class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def diameter_of_binary_tree(root):
    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        diameter_of_binary_tree.result = max(diameter_of_binary_tree.result, left_height + right_height)
        return 1 + max(left_height, right_height)

    diameter_of_binary_tree.result = 0
    height(root)
    return diameter_of_binary_tree.result
