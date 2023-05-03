class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        checker = set()
        for edge in edges:
            checker.add(edge[1])
        return set(range(n)) - checker
        