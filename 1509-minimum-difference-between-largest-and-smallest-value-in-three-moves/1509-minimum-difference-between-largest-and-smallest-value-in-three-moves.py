class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <=4:
            return 0
        nums.sort()
       
        case1 = nums[-4] - nums[0]
        case2 = nums[-1] - nums[3] 
        case3 = nums[-2] - nums[2]
        case4 = nums[-3] - nums[1]
        return min(case1,case2,case3,case4)