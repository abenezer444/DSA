class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        sums={0:1}
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            diff=summ-k
            res+=sums.get(diff,0)
            sums[summ]=1+sums.get(summ,0)
            
            
        return res
        
                
                