class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tb={}
        for idx,num in enumerate(nums):
            if target-num in tb:
                return [idx,tb[target-num]]
            tb[num]=idx
        