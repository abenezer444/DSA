class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = []
        
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                duplicates.append(abs(nums[i]))       
            else:
                nums[abs(nums[i])-1] =  -nums[abs(nums[i])-1]
        return duplicates
                
                
        