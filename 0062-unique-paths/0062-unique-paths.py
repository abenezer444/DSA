class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[0 for i in range(n)] for i in range(m) ]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = 1 + grid [i][j-1] + grid[i-1][j]
        return grid[m-1][n-1] + 1
        
    
        