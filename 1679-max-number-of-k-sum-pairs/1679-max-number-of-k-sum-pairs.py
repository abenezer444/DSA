class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        right=len(nums)-1
        left=0
        count=0
        while left<right:
            if nums[left]+nums[right]>k:
                right-=1
            elif nums[left]+nums[right]<k:
                left+=1
            else:
                count+=1
                right-=1
                left+=1
        return count
            