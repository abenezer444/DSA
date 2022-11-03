class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #ans[2,3,4,-1,-1]
        #[(4,3),(3,4)]
        #while len(stack)>1:
        
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
            
                
        