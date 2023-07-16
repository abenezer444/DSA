class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def isInBound(row,col):
            return row < m and col < n
        def recur(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            if row == m - 1 and col == n - 1:
                return 1
            if not isInBound(row,col):
                return 0
            memo[(row,col)] = recur(row+1,col) + recur(row,col+1)
            return memo[(row,col)]
        return recur(0,0)
    
        