class Solution:
    def prevPermOpt1(self, nums: List[int]) -> List[int]:
        peack = 0
        for i in range(len(nums)-1,0,-1):
           
            if nums[i-1] > nums[i]:
                peack = i-1
                break

        
        peackNum = nums[peack]
        maxAfterPeack = peack + 1
        
        for i in range(peack+1,len(nums)):
            if nums[i] > nums[maxAfterPeack] and nums[i] < peackNum:
                maxAfterPeack = i
        if peack == 0 and maxAfterPeack == len(nums) - 1:
            return nums
        nums[peack],nums[maxAfterPeack] = nums[maxAfterPeack],nums[peack]
        return nums
            

                
                
        
        
        
     
        