class Solution:
    def restoreArray(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        for key in graph:
            if len(graph[key]) == 1:
                start = key
                break
        ans = [start]
        visited = set([start])
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                if child not in visited:
                    ans.append(child)
                    visited.add(child)
                    queue.append(child)
        return ans
                    