class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
        
    def find(self,node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        
        if parent1 != parent2:
            if self.sizes[parent1] > self.sizes[parent2]:
                self.parent[parent2]  = parent1
                self.sizes[parent1] += self.sizes[parent2]
            else:
                self.parent[parent1] = parent2
                self.sizes[parent2] += self.sizes[parent1]
            return True
        return False
    def remove(self, node1, node2):
        if self.sizes[node1] > self.sizes[node2]:
            self.sizes[node1] -= self.sizes[node2]
            self.parent[node2] = node2
        else:
            self.sizes[node2] -= self.sizes[node2]
            self.parent[node1] = node1
            
            
       
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        '7:56'
        union_find = UnionFind(n)
        ans = []
        for a,b in requests:
            parent_a = union_find.find(a)
            parent_b = union_find.find(b)
            union_find.union(a,b)
            
            for c,d in restrictions:
                if union_find.find(c) == union_find.find(d):
                    ans.append(False)
                    union_find.remove(parent_a,parent_b)
                    break
            else:
                ans.append(True)
      
        return ans
            

        