class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        ans = [0] * n 
        graph = defaultdict(list)
        visited = set()
    

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        

        def dfs(node):
            count = Counter(labels[node])
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    count += dfs(neighbour)
            
            ans[node] = count[labels[node]]
            return count
                

           


        dfs(0)

        return ans