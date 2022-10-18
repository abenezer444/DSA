class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #if the remainder is repeated we know forsure the is a segment 
        #that is divisible by k
        #and we want to make sure to check if the segment's length is atleast 2
        remainders={0:-1}
        summ=0
        for idx,num in enumerate(nums):
            summ+=num
            remainder=summ%k
            if remainder not in remainders:
                remainders[remainder]=idx
            elif idx-remainders[remainder]>1:
                return True
            
        return False
        