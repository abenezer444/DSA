class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = defaultdict(int)
        
        def findMin(stair,dp={}):
            
            if stair <= 1:
                return cost[stair]
            if stair in dp:
                return dp[stair]
            else:
                dp[stair] = cost[stair] + min(findMin(stair-1,dp),findMin(stair-2,dp))
            return dp[stair]
                                          
        return min(findMin(len(cost)-1),findMin(len(cost)-2))
        