class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def recur(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            if row == len(triangle) or col == len(triangle[-1]):
                return 0
            minn = 0
            goDown = minn + recur(row+1,col)
            goDownRight = minn + recur(row+1,col+1)
            
            memo[(row,col)] = triangle[row][col] + min(goDown,goDownRight)
            
            return memo[(row,col)]
        return recur(0,0)