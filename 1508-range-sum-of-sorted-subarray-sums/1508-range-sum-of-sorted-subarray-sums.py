class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        for i in range(n):
            summ=nums[i]
            for j in range(i+1,n):
                summ+=nums[j]
                nums.append(summ)
        nums.sort()
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        if left!=1 and right!=1:
            return (nums[right-1]-nums[left-2])%(10**9+7)
        return (nums[right-1])%(10**9+7)
        
            