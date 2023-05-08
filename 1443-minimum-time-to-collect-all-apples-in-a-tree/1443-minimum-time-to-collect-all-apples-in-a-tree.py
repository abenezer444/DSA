class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
       
        visited = set()  
        def dfs(node):
            time = 0
            visited.add(node)
            
            for child in graph[node]:
                
                if child in visited:
                    continue
                childTime = dfs(child)
                
                if childTime or hasApple[child]:
                    time += 2 + childTime
            
            
            return time
        return dfs(0)
        