class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        result=0
        for i in range(n):
            #count in how many times an array can start and end, half of it will have even length and the remaining half odd.
            start=n-i
            end=i+1
            total=start*end+1
            odd=total/2
            result+=odd*arr[i]
        return result
        
        