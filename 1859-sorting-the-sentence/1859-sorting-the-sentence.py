class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        lst=s.split()
        lst.sort(key=lambda i:i[-1])
        for i in range(len(lst)):
            lst[i]=lst[i][:-1]
        return " ".join(lst)
        
        
        