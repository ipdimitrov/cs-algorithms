# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, max_val):
            if node:
                max_val_new = max(max_val, node.val)
                return dfs(node.left, max_val_new) + dfs(node.right, max_val_new) + int(max_val<=node.val)
            return 0
        return dfs(root, float("-inf"))