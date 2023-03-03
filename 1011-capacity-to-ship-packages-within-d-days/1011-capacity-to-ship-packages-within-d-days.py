class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        left = max(ceil(total/days),max(weights))
        right = total
        result = left
        
        while left <= right:
            mid = (right + left)//2
            count = 1
            running_sum = 0
            for num in weights:
                running_sum += num
                if running_sum > mid:
                    count += 1
                    running_sum = num
            if count <= days:
                result = mid
                right = mid - 1
            else:
                left = mid +1
                
        return result
        