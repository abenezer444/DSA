class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        pivot=size-2
        while pivot>=0 and nums[pivot]>=nums[pivot+1]:
            pivot-=1
        if size<=2 or pivot == -1:
            return nums.reverse()
        for i in range(size-1,pivot,-1):
            if nums[pivot]<nums[i]:
                nums[pivot],nums[i]=nums[i],nums[pivot]
                break
        nums[pivot+1:]=reversed(nums[pivot+1:])
        
        