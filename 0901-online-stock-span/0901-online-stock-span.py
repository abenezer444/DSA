class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        ans = 0
    
        while self.stack and self.stack[-1][0] <= price:
            price1, numsLess = self.stack.pop()
            ans += numsLess
        self.stack.append([price , ans + 1])
        
        
        return ans + 1
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)