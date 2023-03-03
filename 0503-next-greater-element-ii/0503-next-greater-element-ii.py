class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums)
        stack=[]
        for idx,num in enumerate(nums):
            while stack and stack[-1][0]<num:
                ans[stack.pop()[1]]=num
            stack.append([num,idx])
        for idx,num in enumerate(nums):
            while stack and stack[-1][0]<num:
                ans[stack.pop()[1]]=num
        
      
        return ans
            
                
        