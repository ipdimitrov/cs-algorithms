# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        def dfs(node, min_val, max_val):
            if node:
                return min_val<node.val and node.val<max_val and dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
            return True
        return dfs(root, float("-inf"), float("+inf"))
        