class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n
        if n==0:
            return 1
        if not n % 2:
            temp=Solution.myPow(self,x,n/2)
            ans= temp*temp
            return ans
        else:
            return x*(self.myPow(x,n-1))
        