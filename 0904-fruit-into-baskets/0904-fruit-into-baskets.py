class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)
        ans = float(-inf)
        left=0
        for right in range(len(fruits)):
            baskets[fruits[right]]+=1
            while len(baskets)>2 and left<len(fruits):
                if baskets[fruits[left]]:
                    baskets[fruits[left]] -= 1
                if not baskets[fruits[left]]:
                    baskets.pop(fruits[left])
                left += 1
            ans = max(right-left+1,ans)
        return ans
            
                
        
            
        