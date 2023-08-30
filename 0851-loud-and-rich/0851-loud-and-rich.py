class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        inDegree = [0]*n
        for e1, e2 in richer:
            graph[e1].append(e2)
            inDegree[e2] += 1
    
        ans = [i for i in range(n)]
        q = deque()
        for i in range(n):
            if inDegree[i] == 0:
                q.append(i)
 

        while q:
            num = q.popleft()
            u = quiet[num]

            for child in graph[num]:
                if u < quiet[child]:
                    quiet[child] = u
                    ans[child] = ans[num]

                inDegree[child]-=1
                if inDegree[child] == 0:
                    q.append(child)

        return ans