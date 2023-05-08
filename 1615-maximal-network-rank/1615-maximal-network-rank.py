class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) == 0:
            return 0 
        if len(roads) == 1:
            return 1
        graph = defaultdict(list)
        
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
       
        ans = 1
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                temp = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    temp -= 1
                ans = max(ans,temp)
        return ans
                    
        
        