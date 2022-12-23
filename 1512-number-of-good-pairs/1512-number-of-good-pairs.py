class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq=Counter(nums)
        total=0
        for num ,count in freq.items():
             total+=math.comb(count,2)
        return total
            
       