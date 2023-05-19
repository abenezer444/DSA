class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i):chr(i) for i in range(ord('a'),ord('z')+1)}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            ra,rb=find(a),find(b)
            if ra == rb:
                return
            parent[ra] = parent[rb] = min(ra, rb)
            
        def isConnected(a,b):
            return find(a) == find(b)
        unEquals = []
        for equation in equations:
            sign = equation[1:-1]
            a = equation[0]
            b = equation[-1]
            if sign == '==':
                union(a,b)
            else:
                unEquals.append((a,b))
        for a,b in unEquals:
            if isConnected(a,b):
                return False
        return True