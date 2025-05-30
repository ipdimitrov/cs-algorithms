# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = 0
        def dfs(node):
            if node is None:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            self.max_sum = max(self.max_sum, l+r)
            return max(l,r) + 1
        dfs(root)
        return self.max_sum