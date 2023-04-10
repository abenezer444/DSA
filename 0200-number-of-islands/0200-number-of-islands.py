class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      
        self.ans = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):
            #base case
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col]=='1':
                    dfs(grid, visited, new_row, new_col)
            
            
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(grid,visited,i,j)
                    self.ans+=1
        return self.ans
        
        
        