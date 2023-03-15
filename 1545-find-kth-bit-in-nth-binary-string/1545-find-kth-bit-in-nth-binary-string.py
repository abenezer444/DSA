class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def finder(n,k):
            if n==1 or k==1:
                return 0
            if k<=2**(n-1)-1:
                return finder(n-1,k)
            elif k==2**(n-1):
                return 1
            else:
                return 1 - finder(n-1,2**(n)-k)
        return str(finder(n,k))

        