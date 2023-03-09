class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums =  [ i for i in range( 1, n + 1)]
        
        def backtrack ( index ,track = []):
            
            
            if len(track) == k:
                result.append( track [:])
                return
            if index >= len(nums):
                return
                
            
            track.append(nums[index])
            backtrack(index + 1,track)
            
            track.pop()
            backtrack(index + 1,track)
        backtrack(0)
        return result
        