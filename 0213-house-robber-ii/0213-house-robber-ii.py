class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        
        
        def recur(i,n,memo):
            maxx = 0
            if i in memo:
                return memo[i]
            if i>=n:
                return maxx
            pick = maxx + nums[i] + recur(i+2,n,memo)
            notPick = maxx + recur(i+1,n,memo)
            maxx = max(pick,notPick)
            memo[i] = maxx
            return memo[i]
        return max(nums[0],recur(0,n - 1,{}),recur(1,n,{}))