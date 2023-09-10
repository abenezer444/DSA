class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        self.maxx = 0
        visited = set()
        length = len(grid)
        width = len(grid[0])
        queue = deque()
        def inbound(row,col):
            return 0 <= row < length  and 0 <= col < width
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        def bfs(row,col):
            
            while queue:
    
                cur = queue.popleft()
                self.maxx = max(cur[2],self.maxx)
                for y,x  in directions:
                    new_row = cur[0] + y
                    new_col = cur[1] + x
                    if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row,new_col,cur[2] + 1))
                        visited.add((new_row,new_col))
        for i in range(length):
            for j in range(width):
                if (i,j) not in visited and grid[i][j] == 2:
                    visited.add((i,j))
                    bfs(i,j)
                    break
                    
   
        
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    return -1
        
        return self.maxx
                    
        