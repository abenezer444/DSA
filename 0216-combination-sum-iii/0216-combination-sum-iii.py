class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        combinations = []
   
        def findCombinations(index, arr, left):
            if left == 0 and len(arr) == k:
                combinations.append(arr.copy())
                return
            
            if index >= len(nums) or left < 0 or len(arr) > k:
                return
            
            vis = set()
            for i in range(index, len(nums)):
                if nums[i] not in vis:
                    arr.append(nums[i])
                    vis.add(nums[i])
                    findCombinations(i + 1, arr, left - nums[i])
                    arr.pop()
            
        if sum(nums) >= target:
            findCombinations(0, [], target)
        
        return combinations
        