class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i:i[0])
        res=[]
        for i in intervals:
            if res and res[-1][1]>=i[0]:
                res[-1][1]=max(i[1],res[-1][1])
            else: res.append(i)
        return res
            