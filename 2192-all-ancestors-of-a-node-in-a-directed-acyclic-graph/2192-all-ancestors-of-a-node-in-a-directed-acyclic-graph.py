class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {node: set() for node in range(n)}
        indegree = {node: 0 for node in range(n)}
        ans = [set() for _ in range(n)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            indegree[edge[1]]+=1
        nodes_with_no_incoming_edges = []
        for node, indeg in indegree.items():
            if indeg == 0:
                nodes_with_no_incoming_edges.append(node)
        while len(nodes_with_no_incoming_edges):
            node = nodes_with_no_incoming_edges.pop()
            for neighbor in graph[node]:
                ans[neighbor].add(node)
                ans[neighbor] = ans[neighbor].union(ans[node])
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    nodes_with_no_incoming_edges.append(neighbor)
                    
        sorted_ans = []           
        for ancestor in ans:
            temp = sorted(list(ancestor))
            sorted_ans.append(temp)
        return sorted_ans
                
                
            
        