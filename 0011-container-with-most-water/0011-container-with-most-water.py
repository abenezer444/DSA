class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        maxArea=0
        while left<right:
            if min(height[left],height[right])*(right-left) > maxArea:
                maxArea=min(height[left],height[right])*(right-left)
            if height[left]<height[right]:
                left+=1
            else: right-=1
        return maxArea
        