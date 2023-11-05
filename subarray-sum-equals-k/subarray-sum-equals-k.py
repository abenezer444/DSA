class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_so_far = defaultdict(int)
        sums_so_far[0] = 1
        cur_sum = 0
        count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in sums_so_far:
                count += sums_so_far[cur_sum - k]
            sums_so_far[cur_sum] += 1
        return count
        
