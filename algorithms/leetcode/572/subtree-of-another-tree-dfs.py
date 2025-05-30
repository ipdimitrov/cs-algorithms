# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        # dfs:
        def isidentical(node, subnode):
            if not node:
                return not subnode
            elif not subnode:
                return False
            return node.val==subnode.val and isidentical(node.left, subnode.left) and isidentical(node.right, subnode.right)
        def dfs (node, subnode):
            if node is None:
                return False
            if isidentical(node, subnode):
                return True
            return dfs(node.left, subnode) or dfs (node.right, subnode)
        return dfs(root, subRoot)
        