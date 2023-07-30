class Solution:
    def numDecodings(self, s: str) -> int:
        
        def isImpossible(prefix):  
            if prefix[0] == '0' or int(prefix) > 26:
                return True
            return False
        @cache
        def recur(i):
            count = 0
            if i >= len(s):
                return count + 1
           
            ans1 = recur(i+1)  if not isImpossible(s[i]) else 0
        
            ans2 = recur(i+2) if i+1 < len(s) and not isImpossible(s[i:i+2]) else 0
            
            count = ans2 + ans1
            
            return count
        return recur(0)
        
        