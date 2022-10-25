class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res=[]
        l=0
        r=len(nums)-1
        while len(nums)!=len(res):
            res.append(nums[l])
            l+=1
            if l<=r:
                res.append(nums[r])
                r-=1
        return res
            
        