class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numbers=nums.copy()
        numbers.sort()
        def leftFinder(target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if numbers[mid]==target:
                    temp=mid
                    right=mid-1
                elif numbers[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return temp
        for idx,num in enumerate(nums):
            nums[idx]=leftFinder(num)
        return nums
            
        