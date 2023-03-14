class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(-1)
        stack = []
        maxArea = 0
        
        for index , height in enumerate(heights):
            
            leftBound = index
            
            while stack and stack[-1][1] > height:
                leftBound , popped = stack.pop()
                maxArea = max(maxArea , (index - leftBound) * popped)
            
            stack.append([leftBound,height])
        
        # for i in range(len(stack)):
        #     leftBound , height = stack[i]
        #     maxArea = max(maxArea , (len(heights) - leftBound)*height  )
        return maxArea
            
            
        
        