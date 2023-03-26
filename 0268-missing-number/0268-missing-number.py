class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i<len(nums):
            j = nums[i]
            if nums[i]<len(nums) and nums[i] != i:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
            
            
        