class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary(left,right):
            if right<left:
                return -1
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(left,mid - 1)
            else:
                return binary(mid+1,right)
        return binary(0,len(nums)-1)