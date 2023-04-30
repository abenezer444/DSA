class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        subIslands = 0
        
        def inbound(row, col):
            return (0 <= row < len(grid2) and 0 <= col < len(grid2[0]))
        
        def dfs(row, col):
            visited.add((row,col))
            grid2[row][col] = 0
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and grid2[new_row][new_col] == 1:
                        dfs(new_row, new_col)
                                      
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and grid1[i][j] == 0 and (i,j) not in visited:
                    dfs(i, j)
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    subIslands+=1
        
                    
        return subIslands