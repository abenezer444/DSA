class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def nthBinaryString(n):
            if n==1:
                return "0"
            temp = nthBinaryString(n-1)
            return temp +'1' + invertRevert(temp)
        def invertRevert(string):
            temp=deque()
            for bit in string:
                if bit=="1":
                    temp.appendleft('0')
                else:
                    temp.appendleft('1')
            return "".join(temp)

        return nthBinaryString(n)[k-1]
    

        
            
            
        
        