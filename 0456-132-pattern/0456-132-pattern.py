class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        find a k value that is less than the top of my stack,my stack being a mono decreasing having the y value at the top and i value somewhere before it
        nums=[3,1,4,2]
        min=1
        [(4,1)]
        
        '''
        stack=[]
        minVal=nums[0]
        for num in nums:
            while stack and stack[-1][0]<=num:
                stack.pop()
            if stack and stack[-1][1]<num:
                return True
            stack.append((num,minVal))
            minVal=min(num,minVal)
        return False
        