class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            cur = bombs[i]
            for j in range(len(bombs)):
                if i!=j:
                    temp = bombs[j]
                    if cur[2]>=((cur[0]-temp[0])**2 + (cur[1]-temp[1])**2)**0.5:
                        graph[i].append(j)
        
        def dfs(node,visited):
            visited.add(node)
            mx = 0
        
            for adj in graph[node]:
                if adj not in visited:
                    mx +=  dfs(adj,visited)
                    
            return mx + 1
        
        maxx = 1
        for node in list(graph.keys()):
            visited = set()
            maxx = max(maxx,dfs(node,visited))
        return maxx
            
            
            
                
        