class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache =  {}
        def recur(left,right):
            if (left,right) in cache:
                return cache[(left,right)]
         
            if right <  left:
                return 0
            elif left == right:
                return 1
            elif s[left] == s[right]:
                cache[(left,right)] = 2  + recur(left + 1, right - 1)
            else:
                cache[(left,right)] =  max(recur(left + 1,right),recur(left,right - 1))
            return cache[(left,right)]
        return recur(0,len(s) - 1)
        