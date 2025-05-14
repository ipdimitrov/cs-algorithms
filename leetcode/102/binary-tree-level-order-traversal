from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        out = []
        while q:
            current_level_values = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    current_level_values.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            out.append(current_level_values)
        return out