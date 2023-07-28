class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def recur(row,col):
            if row == len(triangle) or col == len(triangle[-1]):
                return 0
            minn = 0
            goDown = minn + recur(row+1,col)
            goDownRight = minn + recur(row+1,col+1)
            
            return triangle[row][col] + min(goDown,goDownRight)
        return recur(0,0)