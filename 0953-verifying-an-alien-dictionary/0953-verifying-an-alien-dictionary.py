class Solution:
    def isAlienSorted(self, words: List[str], s: str) -> bool:
        orderMap={s[i]:i for i in range(len(s))}
        inNumber=[]
        for word in words:
            temp=[]
            for letter in word:
                temp.append(orderMap[letter])
            inNumber.append(temp)
        
        for i in range(1,len(inNumber)):
            if  (inNumber[i-1]>inNumber[i]):
                return False
       
        return True
                
        
        
        