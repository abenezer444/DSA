class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,0
        total,res=0,0
        while r<len(nums):
            total+=nums[r]
            #shrink whenever k cannot cover all the values inside the window
            while nums[r]*(r-l+1)>total+k:
                total-=nums[l]
                l+=1
            res=max((r-l+1),res)
            r+=1
        return res
                    
                 
                    
                    

