class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res=0
        even=1
        odd=0
        prefix=0
        for i in arr:
            prefix+=i
            if prefix%2==0:
                even+=1
                res+=odd
            else:
                odd+=1
                res+=even
        return res%(10**9+7)