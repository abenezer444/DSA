class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        threshold1 = float('inf')
        threshold2 = float('inf')
        
        for num in nums:
            if num <= threshold1:
                threshold1 = num
            elif num <= threshold2:
                threshold2  = num
            else:
                return True
        return False
        