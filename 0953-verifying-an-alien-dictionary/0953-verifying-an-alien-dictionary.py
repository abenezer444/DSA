class Solution:
    def isAlienSorted(self, words: List[str], s: str) -> bool:
        orderMap={s[i]:i for i in range(len(s))}
        inNumber=[]
        for word in words:
            temp=[]
            for letter in word:
                temp.append(orderMap[letter])
            inNumber.append(temp)
        
        unsorted=inNumber.copy()   
        inNumber.sort()
       
        return inNumber==unsorted
                
        
        
        