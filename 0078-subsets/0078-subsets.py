class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backTrack(index,arr=[]):
            if index>len(nums):
                return
            subsets.append(arr[:])
            for i in range(index,len(nums)):
                arr.append(nums[i])
                backTrack(i+1,arr)
                arr.pop()
        subsets = []
        backTrack(0)
        return subsets