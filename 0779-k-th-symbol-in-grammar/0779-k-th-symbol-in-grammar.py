class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1 or k == 1:
            return 0
        if k<=2**(n-2):
            return self.kthGrammar(n-1,k)
        else:
            return 1 - self.kthGrammar(n-1,k-2**(n-2))
        