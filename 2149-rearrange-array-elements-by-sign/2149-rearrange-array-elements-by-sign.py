class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[0]*len(nums)
        p=0
        n=1
        for i in nums:
            if i>0:
                output[p]=i
                p+=2
            else:
                output[n]=i
                n+=2
        return output
            
        
        