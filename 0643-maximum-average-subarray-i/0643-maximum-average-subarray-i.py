class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curSum=0
        for index in range(k):
            curSum+=nums[index]
        maxSum=curSum
        start=0
        for index in range(k,len(nums)):
            curSum-=nums[start]
            curSum+=nums[index]
            start+=1
            maxSum=max(maxSum,curSum)
        
            
            
        
        # for index in range(1,len(nums)-k+1):
        #     curSum-=nums[index-1]
        #     curSum+=nums[index+k-1]
        #     maxSum=max(maxSum,curSum)
        return maxSum/k
        