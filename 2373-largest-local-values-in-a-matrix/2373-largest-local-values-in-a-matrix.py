class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        #generate answer
        n=len(grid)
        ans=[[0 for _ in range(n-2)] for _ in range(n-2)]
        temp=[]
        for row in range(1,n-1):
            for col in range(1,n-1):
                top=max(grid[row-1][col-1:col+2])
                mid=max(grid[row][col-1:col+2])
                bottom=max(grid[row+1][col-1:col+2])
                             
                maxx=max(top,mid,bottom)
                ans[row-1][col-1]=maxx
        return ans
        
            
            