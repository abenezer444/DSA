class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        provinces = 0
        visited = set()
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    graph[i].append(j)
        
        def dfs(start,visited):
            if start not in visited:
                visited.add(start)
                for neighbor in graph[start]:
                    dfs(neighbor,visited)
                return
        for start in graph:
            if start not in visited:
                dfs(start,visited)
                provinces+=1
        return provinces
            
        
        
        
        
        