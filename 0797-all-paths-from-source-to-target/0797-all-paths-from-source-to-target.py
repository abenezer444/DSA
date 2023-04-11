class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        target = len(graph) - 1
        def dfs(node,path):
            if node == target:
                output.append(path)
            else:
                for neighbour in graph[node]:
                    dfs(neighbour,path+[neighbour])
        dfs(0,[0])
        return output
                    
                    
                    