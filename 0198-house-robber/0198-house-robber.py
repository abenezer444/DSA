class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1000,100,50,400]
        @cache
        def leba(idx):
            if idx >= len(nums):
                return 0
            return max(nums[idx] + leba(idx+2),leba(idx+1))
        return leba(0)