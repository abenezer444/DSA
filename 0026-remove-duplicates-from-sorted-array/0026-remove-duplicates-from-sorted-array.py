class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ahead=0
        behind=0
        while ahead<len(nums):
            nums[behind] = nums[ahead]
            while ahead<len(nums) and nums[ahead]<=nums[behind] :
                ahead+=1
            behind+=1
        return behind
                
        
        
        
        