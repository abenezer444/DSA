class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def recur(left,right):
         
            if right <  left:
                return 0
            elif left == right:
                return 1
            elif s[left] == s[right]:
                return 2  + recur(left + 1, right - 1)
            else:
                return max(recur(left + 1,right),recur(left,right - 1))
        return recur(0,len(s) - 1)
        