class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        setAlpha=set()
        counter=0
        left=0
        right=0
        while right<len(s):
            #expand, check if char is in my set
            while right<len(s) and s[right] in setAlpha:
                setAlpha.remove(s[left])
                left+=1
            if right<len(s) and s[right] not in setAlpha:
                setAlpha.add(s[right])
            
            if len(setAlpha)==3:
                    counter+=1
                    setAlpha.remove(s[left])
                    left+=1
            
            right+=1
        return counter
        