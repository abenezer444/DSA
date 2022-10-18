class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=0
        for i in range(1,len(nums)):
            pre=nums[i-1]
            if pre>=nums[i]:
                count+=pre-nums[i]+1
                nums[i]=pre+1
        return count
        