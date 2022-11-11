class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def rightFinder():
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r=mid-1
                else:
                    res=mid
                    l=mid+1
            return res
        left=0
        if target>0:
            right=rightFinder()
        else:
            right=len(nums)-1
        while left<right:
            if nums[left]+nums[right]>target:
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                return [left+1,right+1]
            
            
        