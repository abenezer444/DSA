class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations = []
        nums = [i for i in range(1,n+1)]
        
        def findCombinations(index,arr):
            if len(arr) == k:
                combinations.append(arr[:])
                return
            if index >= n:
                return
            arr.append(nums[index])
            findCombinations(index+1,arr)
            arr.pop()
            findCombinations(index+1,arr)
        findCombinations(0,[])
        return combinations
        
        
        