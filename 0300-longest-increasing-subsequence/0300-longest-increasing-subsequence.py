class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def recur(i):
            max_length = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_length = max(max_length, 1 + recur(j))
            return max_length

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, recur(i))
        return ans

            
                
        