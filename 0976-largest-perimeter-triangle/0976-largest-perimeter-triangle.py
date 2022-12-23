class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for right in range(len(nums)-1,1,-1):
            if nums[right]<nums[right-2]+nums[right-1]:
                return nums[right]+nums[right-2]+nums[right-1]
        return 0
        