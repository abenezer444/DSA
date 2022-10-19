class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums=nums
        for i in range(1,len(nums)):
            self.sums[i]=nums[i-1]+nums[i]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left>0 and right>0:
            return self.sums[right]-self.sums[left-1]
        return self.sums[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)