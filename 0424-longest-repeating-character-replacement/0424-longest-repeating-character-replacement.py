class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans=0
        maxFreq=0
        left=0
        countMap={}
        for right in range(len(s)):
            countMap[s[right]]=1+countMap.get(s[right],0)
            maxFreq=max(countMap[s[right]],maxFreq)
            while k+maxFreq <right-left+1 and left<len(s):
                countMap[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
            
                
            
        
        