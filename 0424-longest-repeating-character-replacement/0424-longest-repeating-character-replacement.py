class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res=0
        alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for target in alpha:
            other=0
            l=0
            for r in range(len(s)):
                if s[r]!=target:
                    other+=1
                while other>k:
                    if s[l]!=target:
                        other-=1
                    l+=1
                res=max(res,r-l+1)
        return res

        