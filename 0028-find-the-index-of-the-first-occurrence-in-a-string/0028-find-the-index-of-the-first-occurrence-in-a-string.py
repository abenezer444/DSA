class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        m = len(needle) - 1
        
        
        def addLast(hashvalue,char):
            
            num = ord(char) - ord('a') + 1
            new = hashvalue * 27 + num
            
            return new
        def removeFirst(hashValue,char):
            
            num = ord(char) - ord('a') + 1
            new = hashValue - num*27**(m)
            
            return new
        
        hashNeedle = 0
        for char in needle:
            hashNeedle = addLast(hashNeedle,char)
            
        hashCur =  0
        
        for i in range(len(needle)):
            hashCur = addLast(hashCur,haystack[i])
        
        if hashNeedle == hashCur:
            return 0
        
        for i in range(len(needle),len(haystack)):
            lastIndex = i - len(needle)
            
            hashCur = removeFirst(hashCur,haystack[lastIndex])
            hashCur = addLast(hashCur,haystack[i])
       
            
            if hashCur == hashNeedle:
                
                return i - len(needle) +1
            
        return -1
        
            