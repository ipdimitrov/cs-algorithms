# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val>q.val:
            p, q = q, p
        if p.val<=root.val and root.val<=q.val:
            return root
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)

        