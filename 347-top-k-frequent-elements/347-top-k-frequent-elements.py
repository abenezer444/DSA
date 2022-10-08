class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pairs=collections.Counter(nums)
        pair=[(count,nums) for (nums,count) in pairs.items()]
        heapq._heapify_max(pair)
        res=[]
        for i in range(k):
            res.append(heapq._heappop_max(pair)[1])
        return res
        
        
        
        