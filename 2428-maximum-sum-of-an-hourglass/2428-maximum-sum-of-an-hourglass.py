class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        #function to find the sum of the hour glass
        ans=0
        rows=len(grid)
        column=len(grid[0])
        def summ(i,j):
            return sum(grid[i+1][j-1:j+2])+grid[i][j]+sum(grid[i-1][j-1:j+2])
        #check every possible middle point for the hour glass
        for i in range(1,rows-1):
            for j in range(1,column-1):
                ans=max(ans,summ(i,j))
        return ans
                