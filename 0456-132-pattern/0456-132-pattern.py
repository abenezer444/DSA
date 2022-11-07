class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack=[]
        curMin=nums[0]
        for i in nums[1:]:
            while stack and i>=stack[-1][0]:
                stack.pop()
            if stack and i>stack[-1][1]:
                return True
            stack.append([i,curMin])
            curMin=min(i,curMin)
        return False
        