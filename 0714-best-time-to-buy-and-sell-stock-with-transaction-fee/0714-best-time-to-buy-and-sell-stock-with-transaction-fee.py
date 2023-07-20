class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i,plan):
            ans = 0
            if i == len(prices):
                return ans
            if not plan:
                take =  -prices[i] + dp(i+1,(1+plan)%2) 
            if plan:
                take = prices[i] + dp(i+1,(1+plan)%2) - fee
            notTake = dp(i+1,plan)
            ans = max(take,notTake)
            return ans
        return dp(0,0)
    
        