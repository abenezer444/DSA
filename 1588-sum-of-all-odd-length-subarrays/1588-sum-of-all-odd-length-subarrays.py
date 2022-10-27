class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = sum(arr)
        for i in range(len(arr)-2):
            for j in range(i+3,len(arr)+1,2):
                ans += sum(arr[i:j])
        return ans
        
        