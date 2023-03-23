class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(1,len(nums)+1):
            total += i
        return total - sum(nums)
            
        