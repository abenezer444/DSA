class Solution:
    def findOrder(self, courses: int, pre: List[List[int]]) -> List[int]:
        topOrder = []
        graph = defaultdict(list)
        indegree = [0]*courses
        for a,b in pre:
            graph[b].append(a)
            indegree[a]+=1
        queue = deque()
        for num in range(courses):
            if not indegree[num]:
                queue.append(num)
        while queue:
            start = queue.popleft()
            topOrder.append(start)
            for  child in graph[start]:
                indegree[child] -= 1
                if not indegree[child]:
                    queue.append(child)
        return topOrder if len(topOrder) == courses else []
        
        
        