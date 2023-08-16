#User function Template for python3
import heapq
class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        
        # code here
        ans = []
        window = a[0:k+1]
        heapq.heapify(window)
        for i in range(k+1,len(a)):
            ans.append(heapq.heappop(window))
            heapq.heappush(window,a[i])
        while window:
            ans.append(heapq.heappop(window))
        return ans
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))

# } Driver Code Ends