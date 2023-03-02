class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [-1]*len(nums1)
        indexMap = { num : index for index,num in enumerate(nums1)}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                popped = stack.pop()
                if popped in indexMap:
                    ans[indexMap[popped]] = num
            stack.append(num)
        return ans
            
        