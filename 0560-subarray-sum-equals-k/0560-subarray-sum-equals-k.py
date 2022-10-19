class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result=0
        prefix=0
        hashT={0:1}
        for i in nums:
            prefix+=i
            removedSubArr=prefix-k
            if removedSubArr in hashT:
                result+=hashT[removedSubArr]
            if prefix in hashT:
                hashT[prefix]+=1
            else: hashT[prefix]=1

       
        return result
            
        