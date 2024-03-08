class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefix= [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        def get_splits(_max, prev, sub):
            x = bisect.bisect_right(prefix, _max + prev - sub)
            if x == len(prefix):
                return 1
            return 1 + get_splits(_max + prev - sub, prefix[x - 1], prev)
        
#         def get_splits(max_sum):
            
#             splits = 0
#             cur_sum = 0
            
#             for num in nums:
#                 if cur_sum + num > max_sum:
#                     spilts += 1
#                     cur_sum = num
#                 else:
#                     cur_sum += num
            
#             return splits + 1
        
        left, right = max(nums), sum(nums)
        ans = float('inf')
        while left <= right:
            
            mid = (left + right) // 2
            
            if get_splits(mid, 0, 0) <= k:
                ans = min(ans, mid)
                right = mid - 1
            else:
                # ans = mid
                left = mid + 1
        
        return ans
                
            
        