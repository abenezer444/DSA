class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        heap = [(grid[0][0],(0,0))]
        
        ans = 0
        
        while heap:
            # print(heap)
            
            cost,pos = heappop(heap)
           
            ans = max(cost,ans)
            row,col = pos
            if (row,col) == (len(grid) - 1, len(grid[0]) - 1):
                return cost
            visited.add(pos)
            
            for r,c in directions:
                new_row = row + r
                new_col = col + c
                
                if (new_row,new_col) not in visited and inbound(new_row,new_col):
                 
                    
                    c = max(cost,grid[new_row][new_col])
                    visited.add((new_row,new_col))
                    heappush(heap,(c,(new_row,new_col)))
                
                
        
                