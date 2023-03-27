class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        errorNums = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                errorNums.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        for i in range(len(nums)):
            if nums[i]>0:
                errorNums.append(i+1)
        return errorNums
                
        