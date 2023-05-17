class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ans = []
        rep = {i+1:i+1 for i in range(n)}
        
       
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
                return rep[x]
            return x

         
		
        def union(x, y):
    
            xrep = find(x)
            yrep = find(y)
            if xrep == yrep:
                ans.append([x,y])
            rep[yrep] = xrep

            

        for a,b in edges:
            union(a,b)
        return ans[-1]
        