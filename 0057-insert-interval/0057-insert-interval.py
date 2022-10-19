class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        res=[intervals[0]]
        for i in intervals[1:]:
            if i[0]<=res[-1][1]:
                res[-1][1]=max(res[-1][1],i[1])
            else:
                res.append(i)
        return res
        