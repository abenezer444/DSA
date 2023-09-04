class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            a,b = equations[i]
            weight = values[i]
            graph[a].append([b,weight])
            graph[b].append([a,1/weight])

        
        def pathExists(a,b,visited,product):
            visited.add(a)
            for child,weight in graph[a]:
                if child == b:
                    return product*weight
                if child not in visited:
                    result = pathExists(child,b,visited,product*weight)
                    if result != -1:
                        return result
            return -1
            
        def dfs(a,b):
            if a not in graph or b not in graph:
                return -1
            else:
                return pathExists(a,b,set(),1)
        return [dfs(a,b) for a,b in queries]
            
            
        
            
        