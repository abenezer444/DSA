class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #sort the array and save the index of the first occurence of any unique element.
        table={}
        lst=sorted(nums)
        n=len(nums)
        res=[]
        for i in range(n):
            if lst[i] not in table:
                table[lst[i]]=i
        for i in range(n):
            res.append(table[nums[i]])
        return res
                
        