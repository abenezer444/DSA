class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n ==1 or k==1:
            return 0
        ans = self.kthGrammar(n-1,ceil(k/2))
        if k%2 == 0:
            if ans == 0:
                ans = 1
            else:
                ans = 0
        return ans
        