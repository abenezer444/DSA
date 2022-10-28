class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        #keep track of the index of the smallest elements on the left
        stack=[]
        for i in range(len(nums)):
            if not stack or nums[stack[-1]]>nums[i]:
                stack.append(i)
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                
                ans=max(ans,i-stack.pop())
        return ans