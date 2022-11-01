class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        positives=[]
        negatives=[]
        for i in nums:
            if i<0:
                negatives.append(i)
            else:
                positives.append(i)
        for i in range(len(nums)//2):
            output.append(positives[i])
            output.append(negatives[i])
        return output
        