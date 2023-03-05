class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        temp = 1
        while left<=right:
            mid = (left+right)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                temp = mid
                return temp
            elif nums[mid-1]<nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
        return temp
                
        