class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for start,end,weight in flights:
            graph[start].append([weight,end])
        
        
        
        
        heap = [[0,src,-1]]
        
        visited = set()
        
        while heap:
          
            
            cost,node,step = heappop(heap)
            if (node,step) in visited:
                continue
            
            if node == dst and step <= k:
                return cost
            visited.add((node,step))
           
            
            if node == dst and step <= k:
                return cost
            
            for weight, child in graph[node]:
               
                if step < k:
                    heappush(heap,[cost + weight,child,step + 1])
        return -1
            
            
            
            
        