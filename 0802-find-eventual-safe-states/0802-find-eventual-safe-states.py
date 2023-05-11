class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        invertedGraph = defaultdict(list)
        indegree = defaultdict(int)
        for i,edge in enumerate(graph):
            if not edge:
                queue.append(i)
            for node in edge:
                invertedGraph[node].append(i)
                indegree[i]+=1
        ans = []
      
        while queue:
            cur = queue.popleft()
            ans.append(cur)
          
            for child in invertedGraph[cur]:
                indegree[child] -= 1
                if not indegree[child]:
                    queue.append(child)
        return sorted(ans)
        
        