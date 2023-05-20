class UnionFind:
    def __init__(self, n):
        self.connections = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]

    def find(self, node: int):
        current = node
        while self.connections[current] != current:
            current = self.connections[current]

        root = current
        while self.connections[node] != root:
            node = self.connections[node]
            self.connections[node] = root
        return root

    def union(self, node1: int, node2: int):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return
        
        if self.sizes[root1] > self.sizes[root2]:
            self.sizes[root1] += self.sizes[root2]
            self.sizes[root2] = 1
            self.connections[root2] = root1 
        else:
            self.sizes[root2] += self.sizes[root1]
            self.sizes[root1] = 1
            self.connections[root1] = root2
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x = {}
        y = {}
        n = len(stones)
        union_find = UnionFind(n)

        for i in range(n):
            if stones[i][0] in x:
                union_find.union(i, x[stones[i][0]])
            else:
                x[stones[i][0]] = i

            if stones[i][1] in y:
                union_find.union(i, y[stones[i][1]])
            else:
                y[stones[i][1]] = i
        print(union_find.sizes)
        return sum(i - 1 for i in union_find.sizes)
        