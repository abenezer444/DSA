class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        count=Counter(s)
        maxHeap=[]
        for key,freq in count.items():
            heapq.heappush(maxHeap,[-freq,key])
        while maxHeap:
            count,key=heapq.heappop(maxHeap)
            ans+=key*(-count)
        return ans
        
        