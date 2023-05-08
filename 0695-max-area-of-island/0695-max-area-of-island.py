class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        
        def dfs(row,col):
            
            visited.add((row,col))
            for x,y in directions:
                
                new_row = row + y
                new_col = col + x
                if (new_row,new_col) not in visited and inbound(new_row,new_col) and grid[new_row][new_col] == 1:
                    self.ans += 1
                    dfs(new_row,new_col)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.ans = 1
                    dfs(i,j)
                    ans = max(self.ans,ans)
        return ans
                    
                
        