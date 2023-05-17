class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = {i:i for i in range(n)}
        
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
                return rep[x]
            return x

         
		
        def union(x, y):
            xrep = find(x)
            yrep = find(y)

            rep[yrep] = xrep



        def connected(x, y):
            return find(x) == find(y)
        for a,b in edges:
            union(a,b)
        return connected(source,destination)


        

        