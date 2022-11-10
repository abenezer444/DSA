class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels={'a', 'e', 'i', 'o', 'u'}
        initial=0
        
        for i in range(k):
            if s[i] in vowels:
                initial+=1
        res=initial
        l=0
        for r in range(k,len(s)):
            if s[l] in vowels:
                initial-=1
            l+=1
            if s[r] in vowels:
                initial+=1
            res=max(initial,res)
        return res

        