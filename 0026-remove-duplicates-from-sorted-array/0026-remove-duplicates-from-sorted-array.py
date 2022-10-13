class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 1
        l=0
        r=1
        while nums[l]!=nums[-1] and r<len(nums):
            if nums[l]!=nums[r]:
                nums[l+1],nums[r]=nums[r],nums[l+1]
                l+=1
            r+=1
        return l+1
        