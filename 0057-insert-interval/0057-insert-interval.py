class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        n=len(intervals)
        for i in range(n):
            if newInterval[0]<=intervals[i][0]:
                intervals.insert(i,newInterval)
                break
            else:
                intervals.append(newInterval)
                    
      
        res=[intervals[0]]
        for i in intervals[1:]:
            if i[0]<=res[-1][1]:
                res[-1][1]=max(i[1],res[-1][1])
            else:
                res.append(i)
        return res
                
                    
        