class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n+1)] for _ in range(m+1)]
        paths[0][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                print(i, j)
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m][n]