class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        inDegree = [0] * numCourses
        for u, v in prerequisites:
            graph[u].add(v)
            inDegree[v] += 1

       
        parents = [set() for _ in range(numCourses)]
        q = deque([node for node in range(numCourses) if not inDegree[node]])
        while q:
            node = q.popleft()
            parents[node].add(node)
            for nxt in graph[node]:
                inDegree[nxt] -= 1
                parents[nxt] = parents[nxt].union(parents[node])
                if not inDegree[nxt]:
                    q.append(nxt)

        
        ans = []
        for u, v in queries:
            if u in parents[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans