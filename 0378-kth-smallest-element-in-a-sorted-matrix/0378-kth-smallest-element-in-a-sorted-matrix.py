class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums=[]
        for i in matrix:
            nums.extend(i)
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return  heapq.heappop(nums)
            
            
            
        