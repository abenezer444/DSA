class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
        
        
        """
        queue=deque()
        for index in range(len(nums)):
            if  nums[index] and queue:
                nums[queue.popleft()]=nums[index]
                nums[index]=0
                queue.append(index)
            elif nums[index]==0:
                queue.append(index)
                
        