class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def nthBinaryString(n):
            if n==1:
                return "0"
            return nthBinaryString(n-1) +'1' + invertRevert(nthBinaryString(n-1))
        def invertRevert(string):
            temp=[]
            for bit in string:
                if bit=="1":
                    temp.append('0')
                else:
                    temp.append('1')
            return "".join(temp[::-1])

        return nthBinaryString(n)[k-1]
    

        
            
            
        
        