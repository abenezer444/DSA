class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        sweep = [0]*len(nums)
        for request in requests:
            start,end=request
            sweep[start] += 1
            if end<len(nums)-1:
                sweep[end+1] -= 1
    
        for i in range(1,len(sweep)):
            sweep[i] += sweep[i-1]
        nums.sort(reverse=True)
        sweep.sort(reverse=True)
        ans=0
        for idx,num in enumerate(sweep):
            ans += nums[idx]*num
            if num==0:
                break
        return ans%(10**9+7)
        
        