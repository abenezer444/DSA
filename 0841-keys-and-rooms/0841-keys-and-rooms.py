class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])
        
        while queue:
            
            node = queue.popleft()
            visited.add(node)
            
            for neighbour in rooms[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
        for i in range(1,len(rooms)):
            if i not in visited:
                return False
        return True
                    
        
        
        
        