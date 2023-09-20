class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    
        @cache
        def recur(left,right,index):
            if index >= len(multipliers):
                return 0
            
            
            
            leftSum = (nums[left] * multipliers[index]) + recur(left + 1, right, index + 1)
            rightSum = (nums[right] * multipliers[index]) + recur(left , right - 1, index + 1)
            return max(leftSum,rightSum)
        return recur(0,len(nums) - 1, 0)
                
                
        