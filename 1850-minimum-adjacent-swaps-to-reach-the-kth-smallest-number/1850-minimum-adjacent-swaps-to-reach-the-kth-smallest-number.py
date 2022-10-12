class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        count=0
        nums=[digit for digit in num]
        def helper(nums):
            size=len(nums)
            pivot=size-2
            while pivot>=0 and nums[pivot]>=nums[pivot+1]:
                pivot-=1
            if size<=2 or pivot == -1:
                return nums.reverse()
            for i in range(size-1,pivot,-1):
                if nums[pivot]<nums[i]:
                    nums[pivot],nums[i]=nums[i],nums[pivot]
                    break
            nums[pivot+1:]=reversed(nums[pivot+1:])
            return nums
        for i in range(k):
            helper(nums)
        #find the index of the first unmatching num, then substract it form the last index
        for i in range(len(nums)-1):
            if nums[i]!=num[i]:
                r=i+1
                while nums[r]!=num[i]:
                    r+=1
                while r!=i:    
                    nums[r],nums[r-1]=nums[r-1],nums[r]
                    count+=1
                    r-=1
        return count
                
            
        