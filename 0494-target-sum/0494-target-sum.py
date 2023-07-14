class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def recur(index,current):
            if index==len(nums):
                if current==target:
                    return 1
                return 0
            return recur(index+1,current+nums[index])+recur(index+1,current-nums[index])
        return recur(0,0)