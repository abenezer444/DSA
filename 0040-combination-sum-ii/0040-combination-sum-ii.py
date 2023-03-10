class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        checker = []
        nums.sort()
        def findCombinations(index, arr, left):
            if left == 0:
                checker.append(arr.copy())
                return
            
            if index >= len(nums) or left < 0:
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
        
        return checker