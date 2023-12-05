class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashT={}
        for i in range(len(nums)):
            num=target-nums[i]
            if nums[i] in hashT.keys():
                return [hashT[nums[i]],i]
            else: hashT[num]=i
        