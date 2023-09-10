class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        length = len(heights)
        width = len(heights[0])
        directions = [(1,0),(0,-1),(0,1),(-1,0)]
        def inbound(row,col):
            return 0 <= row < length and 0 <= col < width
        def bfs(row,col,visited):
            queue = deque([(row,col)])
            
            while queue:
                vertical,horizontal = queue.popleft()
                
                for y,x in directions:
                    new_row,new_col = vertical + y,horizontal + x
                    if inbound(new_row,new_col) and  (new_row,new_col) not in visited:
                        if heights[vertical][horizontal] <= heights[new_row][new_col]:
                            visited.add((new_row,new_col))
                            queue.append((new_row,new_col))
        pacific = set()
        atlantic = set()
        for i in range(length):
            pacific.add((i,0))
            bfs(i,0,pacific)
        for i in range(width):
            pacific.add((0,i))
            bfs(0,i,pacific)
            
        for i in range(length):
            atlantic.add((i,width - 1))
            bfs(i,width - 1,atlantic)
        for i in range(width):
            atlantic.add((length - 1,i))
            bfs(length - 1,i,atlantic)
        return list(pacific & atlantic)
                
        