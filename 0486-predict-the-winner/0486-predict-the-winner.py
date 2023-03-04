class Solution:
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def take(left,right):
            if left == right:
                return nums[left]
            return max((nums[left]-take(left+1,right)),(nums[right]-take(left,right-1)))
        
        return take(0,len(nums)-1) >= 0
    
        