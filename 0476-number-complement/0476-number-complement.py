class Solution:
    def findComplement(self, num: int) -> int:
        checker = 0
        bit_mask = 1
        while bit_mask <= num:
            checker += bit_mask
            bit_mask  <<= 1
            
            
        return (checker)^num
        