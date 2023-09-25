class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = list(zip(scores,ages))
        
        pairs.sort()
        dp = [pairs[i][0] for i in range(len(pairs))] 
       
        
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] <= pairs[i][1]:
                    dp[i] = max(dp[i], pairs[i][0] + dp[j])

        print(pairs)
        print(dp)
        return max(dp)
    
        
        