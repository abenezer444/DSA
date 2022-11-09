class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        nums=str(num)
        l=0
        count=0
        while k+l<=len(nums):
            if int(nums[l:k+l]) and num%int(nums[l:k+l])==0:
                count+=1
            l+=1
        return count
            
        