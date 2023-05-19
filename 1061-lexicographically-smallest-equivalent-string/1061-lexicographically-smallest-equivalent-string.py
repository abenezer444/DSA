
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i):chr(i) for i in range(ord('a'),ord('z')+1)}
        
        def find(e):
            if parent[e]!=e:
                parent[e] = find(parent[e])
            return parent[e] 

        def union(a,b):
            ra,rb=find(a),find(b)
            if ra == rb:
                return
            parent[ra] = parent[rb] = min(ra, rb)
        
        for c1,c2 in zip(s1,s2): union(c1,c2) 
        return ''.join(parent[find(c)] for c in baseStr)
        
