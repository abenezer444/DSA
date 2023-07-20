class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i,plan):
            ans = 0
            if (i,plan) in memo:
                return memo[(i,plan)]
            if i == len(prices):
                return ans
            if not plan:
                take =  -prices[i] + dp(i+1,(1+plan)%2) 
            if plan:
                take = prices[i] + dp(i+1,(1+plan)%2) - fee
            notTake = dp(i+1,plan)
            ans = max(take,notTake)
            memo[(i,plan)] = ans
            return memo[(i,plan)]
        return dp(0,0)
    
        