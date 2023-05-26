class Solution(object):
    def helper(self, n, data):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
		
        if n in data:
            return data[n]
        
	
        data[n] = self.helper(n-1, data) + self.helper(n-2, data)
        return data[n]
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.helper(n, {})