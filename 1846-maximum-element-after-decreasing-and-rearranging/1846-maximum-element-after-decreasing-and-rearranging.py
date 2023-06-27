class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        ans = 1
        arr.sort()
        for num in arr[1:]:
            if num > ans:
                ans+=1
        return ans
    
        