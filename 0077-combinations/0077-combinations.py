class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums =  [ i for i in range( 1, n + 1)]
        
        def backtrack ( index , k , track = []):
            
            if index >= len(nums):
                
                if len(track) == k:
                    result.append( track [:])
                
                return
            
            track.append(nums[index])
            backtrack(index + 1, k, track)
            
            track.pop()
            backtrack(index + 1, k, track)
        backtrack(0,k)
        return result
        