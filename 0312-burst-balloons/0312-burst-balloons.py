class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        
        nums  = [1] + nums + [1]
        
        
        def backtrack(left,right):
            
            if left > right:
                return 0
            
            if (left,right) in dp:
                return dp[(left,right)]
            
            for i in range(left, right + 1):
                
                coins = nums[i] * nums[left - 1] * nums[right + 1]
                
                left_part =  backtrack(left, i - 1)
                right_part = backtrack(i + 1, right)
                
                dp[(left, right)] = max(dp[(left,right)], coins + left_part + right_part)
            
            return dp[(left,right)]
        
        return backtrack(1, len(nums) - 2)