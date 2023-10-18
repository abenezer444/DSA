class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        parent = [i for i in range(n)]
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 != parent2:
                parent[parent1] = parent2
                
        queries_indexed = []
        
        for index,query in enumerate(queries):
            
            node1, node2, weight = query
            
            queries_indexed.append([index, node1, node2, weight])
      
                
        edgeList.sort(key = lambda x:x[2])
        
        queries_indexed.sort(key = lambda x:x[-1])
       
        
        possible_index = 0
        
        ans = [False] * len(queries)
        
        for index, node1, node2, weight in queries_indexed:
          
            
            while possible_index < len(edgeList) and weight > edgeList[possible_index][2]:
                
                union(edgeList[possible_index][0],edgeList[possible_index][1])
                possible_index += 1
                
            if find(node1) == find(node2):
                ans[index] = True
        return ans
        
        
        