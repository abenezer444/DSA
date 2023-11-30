class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = [i for i in range(len(s) + 1)]
        
        for i in range(len(s)):
            
            
            for j in range(i + 1):
                
                word = s[j:i+1]
                
                if word in words:
                    dp[i+1] = min(dp[i+1],dp[j])
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        return dp[-1]
                
                
        