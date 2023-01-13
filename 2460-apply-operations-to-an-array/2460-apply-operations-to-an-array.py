class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)-1):
            if nums[index]==nums[index+1]:
                nums[index]*=2
                nums[index+1]=0
    
        write=0
        for read in range(len(nums)):
            if nums[read]:
                nums[write],nums[read]=nums[read],nums[write]
                write+=1
        return nums
            
        