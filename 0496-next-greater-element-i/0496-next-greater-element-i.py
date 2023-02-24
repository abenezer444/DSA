class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums1)
        indexMap={num:idx for idx,num in  enumerate(nums1)}
        for i in range(len(nums2)):
            if nums2[i] in indexMap:
                temp=nums2[i]
                while i<len(nums2):
                    if nums2[i]>temp:
                        ans[indexMap[temp]]=nums2[i]
                        break
                    i+=1
        return ans
            
        