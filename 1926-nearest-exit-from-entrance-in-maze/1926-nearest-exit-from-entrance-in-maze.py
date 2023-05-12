class Solution:
    def nearestExit(self, grid: List[List[str]], entrance: List[int]) -> int:
        def isExit(row,col):
            return row == len(grid) - 1 or row == 0 or col == len(grid[0])-1 or col == 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
        visited = set([tuple(entrance)])
        
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
            
        queue = deque([[entrance[0], entrance[1],0]])

        while queue:

            row, col, depth = queue.popleft()

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row,new_col) and grid[new_row][new_col] == '.':
                    
                    if (new_row,new_col) not in visited:
                        if isExit(new_row,new_col):
                            return depth+1
                        queue.append([new_row,new_col,depth+1])
                        visited.add((new_row,new_col))
        return -1
        