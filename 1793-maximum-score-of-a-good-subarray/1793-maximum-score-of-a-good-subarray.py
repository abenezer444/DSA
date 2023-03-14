class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = k
        right = k
        minNum = nums[k]
        maxScore = nums[k]
        
        
        while (left > 0) or right < (len(nums) - 1):
            if left > 0 and right < len(nums) - 1:
                if nums[left - 1] >= nums[right + 1]:
                    left -= 1
                    minNum = min(minNum,nums[left])
                else:
                    right += 1
                    minNum = min(minNum,nums[right])
            elif (left > 0):
                left -= 1
                minNum = min(minNum,nums[left])
            else:
                right += 1
                minNum = min(minNum,nums[right])
            
            maxScore = max(maxScore,minNum * (right - left + 1))
        return maxScore
            
            
                
                
                    

        