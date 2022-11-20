class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        numsMap=set()
        for num in nums1:
            numsMap.add(num)
        for num in nums2:
            if num in numsMap:
                res.append(num)
                numsMap.remove(num)
        return res
        