class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        
    def find(self, node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        
        if parent1 ==  parent2:
            return True
        self.parent[parent1] = self.parent[parent2]
        return False


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        union = UnionFind(n)
        
        indexed = []
        
        for index, edge in enumerate(queries):
            a, b, weight = edge
            indexed.append((weight,a,b,index))
        indexed.sort()
        
        edgeList.sort(key = lambda x:x[2])
        
        ans = [False]*len(queries)
        
       
        cur_index = 0
       
        for weight,a,b,index in indexed:
            
            while cur_index < len(edgeList) and weight > edgeList[cur_index][-1]:
                
                
                union.union(edgeList[cur_index][0],edgeList[cur_index][1])
                cur_index += 1
            
            
            if union.find(a) == union.find(b):
                ans[index] = True
        return ans
            
    
                
        
            
        
        
        
        
        