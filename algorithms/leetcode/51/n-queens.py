class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        current_board = [["." ]*n for _ in range(n)]
        def rec(i):
            if i == n:
                copy = ["".join(row) for row in current_board]
                out.append(copy)
                return
            for j in range(n):
                current_board[i][j] = "Q"
                if check_board(i,j):
                    rec(i+1)
                current_board[i][j] = "."
        def check_board(i, j):
            for k in range(n):
                if j!=k and current_board[i][k] == "Q":
                    return False
            for k in range(n):
                if i!=k and current_board[k][j] == "Q":
                    return False
            k = 0
            while k<n and k+j-i<n:
                if k+j-i>-1 and k!=i and current_board[k][k+j-i] == "Q":
                    return False
                k+=1
            k = 0
            while k<n and i + j - k >-1:
                if i + j - k<n and k!=i and current_board[k][i + j - k] == "Q":
                    return False
                k+=1
            return True
        rec(0)
        return out