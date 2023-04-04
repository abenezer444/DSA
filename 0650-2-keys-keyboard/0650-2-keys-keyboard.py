class Solution:
    def minSteps(self, n: int) -> int:
        minops = 0
        d = 2

        while d * d <= n:
            while n % d == 0:
                minops+=d
                n //= d
            d += 1
        if n > 1:
            minops+=n
        return minops

        