class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            n &= n - 1
            bits += 1
        return bits
        
        