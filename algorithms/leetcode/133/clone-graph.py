# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_map = {}
        node_map[node] = Node(node.val)
        q = deque([node])
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                node_map[cur].neighbors.append(node_map[neighbor])
        return node_map[node]