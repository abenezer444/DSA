class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key=lambda t:t[1])
        events=[0]*1001
        for trip in trips:
            events[trip[1]]+=trip[0]
            events[trip[2]]-=trip[0]
        maxx=0
        for i in events:
            maxx+=i
            if maxx>capacity:
                return False
        return True

        
        
        
        