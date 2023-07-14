class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def recur(index, current):
            if (index, current) in memo:
                return memo[(index, current)]
            if index == len(nums):
                if current == target:
                    return 1
                return 0
            memo[(index, current)] = recur(index + 1, current + nums[index]) + recur(index + 1, current - nums[index])
            return memo[(index, current)]
        return recur(0,0)
