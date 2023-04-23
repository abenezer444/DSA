class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        saviours = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
       
            
        
        def onBorder(row,col):
            if inbound:
                return (row == 0 or row == len(grid) - 1) or (col == 0 or col == len(grid[0]) - 1)
            return False
        
            
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        
        def dfs(grid, visited, row, col):
            
            visited[row][col] = True
            if onBorder(row,col) and grid[row][col] == 'O':
                saviours.add((row,col))
            
            for row_change, col_change in directions:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    if (row,col) in saviours and grid[new_row][new_col] == 'O' :
                        saviours.add((new_row,new_col))
                        
                        dfs(grid, visited, new_row, new_col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O' and onBorder(i,j):
                    saviours.add((i,j))
        
        for saviour in list(saviours):
            dfs(grid,visited,saviour[0],saviour[1])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in saviours:
                    grid[i][j] = 'X'
        
                    
        return grid
