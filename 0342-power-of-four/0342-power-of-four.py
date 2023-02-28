class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0 and int((log(n)/log(4))) == (log(n)/log(4)) :
            return True
        return False
        