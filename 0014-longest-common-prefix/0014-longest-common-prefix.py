class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp=len(strs[0])
        for i in range(1,len(strs)):
            temp=0
            end=min(lcp,len(strs[i]))
            for j in range(end):
                if strs[0][j]==strs[i][j]:
                    temp+=1
                else: 
                    break
            lcp=min(lcp,temp)
        
        return strs[0][:lcp]
                
            
                    
        