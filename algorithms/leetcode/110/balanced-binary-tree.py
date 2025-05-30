from typing import Optional
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs (node):
            if node is None:
                return 0
            l,r = dfs(node.left), dfs(node.right)
            return float("-inf") if abs(l-r) >1 else max(l,r)+1
        return dfs(root)>-1