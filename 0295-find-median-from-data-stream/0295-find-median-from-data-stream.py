class MedianFinder:
    def __init__(self):
        self.lowMax = []
        self.highMin = []

    def addNum(self, num: int) -> None:
        if(len(self.lowMax) == 0):
            heapq.heappush(self.lowMax, -num)
        elif(-self.lowMax[0] >= num):
            heapq.heappush(self.lowMax, -num)
        else:
            heapq.heappush(self.highMin, num)
        if(len(self.lowMax) - len(self.highMin) >= 2):
            heapq.heappush(self.highMin, -heapq.heappop(self.lowMax))
        if(len(self.highMin) - len(self.lowMax) >= 2):
            heapq.heappush(self.lowMax, -heapq.heappop(self.highMin))

    def findMedian(self) -> float:
        if(len(self.lowMax) == len(self.highMin)):
            return((-self.lowMax[0] + self.highMin[0]) / 2)
        return(-self.lowMax[0] if len(self.lowMax) > len(self.highMin) else self.highMin[0])