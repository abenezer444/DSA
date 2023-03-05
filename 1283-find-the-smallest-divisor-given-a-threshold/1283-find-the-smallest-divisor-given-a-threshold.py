class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def getSum(divisor):
            result = 0
            for num in nums:
                result += ceil(num/divisor)
            return result
        left,right = 1,max(nums)
        temp = max(nums)
        while left<=right:
            mid = (right+left)//2
            if getSum(mid) > threshold:
                left = mid+1
            else:
                temp = mid
                right = mid-1
        return temp