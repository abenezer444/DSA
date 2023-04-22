class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        
        colors = [-1] * len(graph)
        
        
        
        for i in range(len(graph)):
            if colors[i] == -1:
                queue = deque([i])
                colors[i] = 1
               
                while queue:
                    node = queue.popleft()
                    
                  
                    for curNode in graph[node]:
                        if colors[curNode] == -1:
                            queue.append(curNode)
                            colors[curNode] = 1 - colors[node]
                        elif colors[curNode] == colors[node]:
                            return False
         
     
        return True
            
            
            
            
            
            
        
        
        
        