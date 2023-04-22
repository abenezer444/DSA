class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for edge in dislikes:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        
        colors = [-1] * (n+1)
        
        
        for i in list(graph.keys()):
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
        
        