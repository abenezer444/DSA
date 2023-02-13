class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numbers=list(map(str,nums))
        nums=[int(num) for num in nums]
        nums=set(nums)
        for num in numbers:
            nums.add(int(num[::-1]))
 
        return len(nums)
        
        