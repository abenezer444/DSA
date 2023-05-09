class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        result = [[-1] * len(mat[0]) for _ in range(len(mat))]
        
        queue = deque()
        visited = set()
        
        def inbound(row,col):
            return 0<=row<len(mat) and 0<=col<len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append(((i,j),0))
                    visited.add((i,j))
                
        
        while queue:
            pos,depth = queue.popleft()
            
            
            result[pos[0]][pos[1]] = depth
            for x,y in directions:
                new_row = y + pos[0]
                new_col = x + pos[1]
                if inbound(new_row,new_col)  and (new_row,new_col) not in visited:
                    queue.append(((new_row,new_col),depth + 1))
                    visited.add((new_row,new_col))
        return result
            