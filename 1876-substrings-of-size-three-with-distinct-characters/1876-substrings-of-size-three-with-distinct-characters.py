class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)-2):
            string=s[i]
            for j in range(i+1,i+3):
                if s[j] in string:
                    break
                string+=s[j]
            if len(string)==3:
                count+=1
        return count
                