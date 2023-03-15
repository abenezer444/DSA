class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        monoQueue = deque()
        
        maxNums = []
        
        for index,num in enumerate(nums):
            while monoQueue and monoQueue[-1][0] < num:
                monoQueue.pop()
            monoQueue.append([num,index])
            if index + 1 >= k:
                if index - monoQueue[0][1] >= k:
                    monoQueue.popleft()
                maxNums.append(monoQueue[0][0])
            
                
                
                
        return maxNums
            
        
        
        