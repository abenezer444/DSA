class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        
        maxNum = nums[0]
        
        for num in nums:
            points[num] += num
            maxNum = max(maxNum,num)
        ans = [0] * (maxNum + 1)
        ans[1] = points[1]
        for i in range(2, maxNum + 1):
            ans[i] = max(ans[i-1],ans[i-2] + points[i])
        return ans[maxNum]
        
        