class Solution:
    def getSatisfaction(self,extent,arr):
        summ = 0
        for i in range(extent):
            summ += arr[i]*(extent - i)
        return summ
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        maxx = 0
        
        for i in range(1,len(satisfaction)+1):
            maxx = max(maxx,self.getSatisfaction(i,satisfaction))
        return maxx
        
        