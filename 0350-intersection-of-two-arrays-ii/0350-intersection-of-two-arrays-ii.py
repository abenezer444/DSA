class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        num1=False
        num2=False
        if len(nums1)>len(nums2):
            num1=True
        else:
            num2=True
        if num1:
            countMap=Counter(nums2)
            for num in nums1:
                if num in countMap and countMap[num]>0:
                    res.append(num)
                    countMap[num]-=1
        else:
            countMap=Counter(nums1)
            for num in nums2:
                if num in countMap and countMap[num]>0:
                    res.append(num)
                    countMap[num]-=1
        return res
                    
                    
                    
                
        