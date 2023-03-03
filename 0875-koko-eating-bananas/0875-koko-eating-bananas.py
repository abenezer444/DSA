class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return ceil(piles[0]/h)
        piles.sort()
        if len(piles) == h:
            return piles[-1]
        right = piles[-2]
        left = piles[-1]/(h-len(piles)+1)
        temp = right
        right = ceil(max(left,right))
        left = int(min(temp,left))
        temp = right
        while left <= right:
        
            mid = (left + right)//2
            result = 0
            for index in range(len(piles)):
                result += ceil((piles[index])/mid)
            if result > h:
                left = mid + 1
            else:
                temp = mid
                right = mid - 1
        
        return temp
                
            
            
        