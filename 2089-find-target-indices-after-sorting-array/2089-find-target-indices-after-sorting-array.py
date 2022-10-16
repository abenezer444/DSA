class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        res=-1
        l=0
        n=len(nums)
        r=n-1
        #find the left most occurence
        while l<=r:
            mid=(l+r)/2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                res=mid
                r=mid-1
        left=res
        print(left)
        res=-1
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)/2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                res=mid
                l=mid+1
        right=res
        print(right)
        if nums[res]==target:
            return [i for i in range(left,right+1)]
        return []
        
                