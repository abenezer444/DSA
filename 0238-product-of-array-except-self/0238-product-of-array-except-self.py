class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[1]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            pre[i]=nums[i-1]*pre[i-1]
        post=[1]*(len(nums)+1)
        for i in  range(len(nums)-1,-1,-1):
            post[i]=nums[i]*post[i+1]
        res=[]
        for i in range(len(nums)):
            res.append(pre[i]*post[i+1])
        return res
        