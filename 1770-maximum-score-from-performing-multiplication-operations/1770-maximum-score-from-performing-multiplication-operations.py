class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    
        dp = {}
        def recur(left,right,index):
            if (left,right) in dp:
                return dp[(left,right)]
            if index >= len(multipliers):
                return 0
            
            
            
            leftSum = (nums[left] * multipliers[index]) + recur(left + 1, right, index + 1)
            rightSum = (nums[right] * multipliers[index]) + recur(left , right - 1, index + 1)
            dp[(left,right)] = max(leftSum,rightSum)
            return dp[(left,right)]
        return recur(0,len(nums) - 1, 0)
                
                
        