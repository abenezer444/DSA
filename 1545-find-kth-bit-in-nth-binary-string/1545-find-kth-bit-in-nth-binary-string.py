class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def nthBinaryString(n):
            if n==1:
                return "0"
            return nthBinaryString(n-1) +'1' + invertRevert(nthBinaryString(n-1))
        def invertRevert(string):
            temp=deque()
            for bit in string:
                if bit=="1":
                    temp.appendleft('0')
                else:
                    temp.appendleft('1')
            return "".join(temp)

        return nthBinaryString(n)[k-1]
    

        
            
            
        
        