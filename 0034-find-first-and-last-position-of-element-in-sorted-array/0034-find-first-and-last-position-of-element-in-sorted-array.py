class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
    
            
        left = bisect_left(nums,target,0,len(nums)-1)
        right = bisect_right(nums,target,0,len(nums))
        if nums[right-1] == target:
            right -= 1
        else:
            right = -1
        if nums[left]!=target:
            left = -1
            
        return [left,right]