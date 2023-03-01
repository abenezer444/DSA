class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        curSum = 0
        sumCountMap=defaultdict(int)
        sumCountMap[0] = 1
        for right in range(len(nums)):
            
            
            curSum += nums[right]
            diff = curSum - k

            count += sumCountMap[diff]
            sumCountMap[curSum] += 1
        return count
            
            
        