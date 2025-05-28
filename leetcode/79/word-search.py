from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        used = []
        def dfs (i, j, k_len):
            if k_len == len(word):
                return True
            used.append((i,j))
            var = False
            if i+1<m and (i+1,j) not in used and board[i+1][j]==word[k_len]:
                var += dfs (i+1, j, k_len+1)
            if j+1<n and (i,j+1) not in used and board[i][j+1]==word[k_len]:
                var += dfs (i, j+1, k_len+1)
            if i>0 and (i-1,j) not in used and board[i-1][j]==word[k_len]:
                var += dfs (i-1, j, k_len+1)
            if j>0 and (i,j-1) not in used and board[i][j-1]==word[k_len]:
                var += dfs (i, j-1, k_len+1)
            used.pop()
            return var
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and dfs(i, j, 1):
                    return True
        return False