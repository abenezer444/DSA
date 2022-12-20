class Solution:
    def freqAlphabets(self, s: str) -> str:
        l=0
        r=2
        ans=""
        length=len(s)
        while r<length:
            if s[r]=='#' and r<length:
                ans+=chr(96+int(s[l:r]))
                l+=3
                r+=3
            else:
                ans+=chr(96+int(s[l]))
                l+=1
                r+=1
        while l<length:
            ans+=chr(96+int(s[l]))
            l+=1
            
        return ans
                
                
        