class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sMap={}
        for letter in s:
            if letter in sMap:
                sMap[letter]+=1
            else:
                sMap[letter]=1
        tMap={}
        for letter in t:
            if letter in tMap:
                tMap[letter]+=1
            else:
                tMap[letter]=1
        
        for letter in tMap.keys():
            if letter in sMap:
                if sMap[letter]!=tMap[letter]:
                    return letter
            else:
                return letter
        
        