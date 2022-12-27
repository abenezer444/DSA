class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], extra: int) -> int:
        minheap=[]
        ans=0
        for i in range(len(rocks)):
            heappush(minheap,capacity[i]-rocks[i])
        while minheap and minheap[0]<=extra and extra:
            if extra-minheap[0] >= 0:
                ans+=1
                extra-=heappop(minheap)
        return ans
        
            
        