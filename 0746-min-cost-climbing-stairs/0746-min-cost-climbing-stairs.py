class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        ans = [float('inf')] * (len(cost))
        ans[0] = cost[0]
        ans[1] = cost[1]
        for i in range(2, len(cost)):
            ans[i] = min(ans[i-1],ans[i-2]) + cost[i]
        
        return min(ans[-1],ans[-2])

        