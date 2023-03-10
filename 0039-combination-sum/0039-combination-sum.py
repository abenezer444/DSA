class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        target1 = target
        combinations = []
        
        
        def findCombinations(index,arr,target):
            
            if target==0:
                combinations.append(arr[:])
                return
            if index >= len(nums):
                return
            
            if target-nums[index]>=0:
                arr.append(nums[index])
                findCombinations(index,arr,target-nums[index])
                arr.pop()
            findCombinations(index+1,arr,target)
        findCombinations(0,[],target)
        return combinations
        