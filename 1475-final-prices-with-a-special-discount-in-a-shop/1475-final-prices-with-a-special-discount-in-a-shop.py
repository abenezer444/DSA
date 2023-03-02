class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0] * len(prices)
        stack = []
        for index,price in enumerate(prices):
            while stack and prices[stack[-1]]>=price:
                idx = stack.pop()
                ans[idx] = prices[idx]-price
        
            stack.append(index)
        for index in stack:
            ans[index] = prices[index]
        return ans
            
        