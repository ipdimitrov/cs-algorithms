from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter_islands+=1
                    d = deque()
                    d.append((i,j))
                    while d:
                        ic, jc = d.popleft()
                        if ic>=0 and jc>=0 and ic<len(grid) and jc<len(grid[0]) and grid[ic][jc] == "1":
                            d.extend([(ic+1,jc),(ic-1,jc),(ic,jc-1),(ic,jc+1)])
                            grid[ic][jc] = "0"
        return counter_islands