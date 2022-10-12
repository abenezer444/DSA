class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxx=0
        res=0
        for i in s:
            if i==']':
                maxx+=1
            else: maxx-=1
            res=max(maxx,res)
        return (res+1)/2
            
        