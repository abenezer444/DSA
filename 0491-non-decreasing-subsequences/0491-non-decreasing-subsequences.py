class Solution:
    def backtrack(self,index,arr):
        
        
        
        if len(arr) >= 2 and tuple(arr) not in self.visited:
            self.ans.append(arr[:])
            self.visited.add(tuple(arr))
            
        if index >= len(self.nums):
            return
            
        if not arr or (arr and self.nums[index] >= arr[-1]):
            arr.append(self.nums[index])
            self.backtrack(index+1,arr)
            arr.pop()
            
        self.backtrack(index+1,arr)
            
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.nums = nums
        self.visited = set()
        self.ans = []
        self.backtrack(0,[])
        return self.ans
        
        