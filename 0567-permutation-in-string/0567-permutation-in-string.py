class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        asDict=Counter(s1)
        sliding=defaultdict(int)
        if len(s2)<len(s1):
            return False
        for index in range(len(s1)):
            sliding[s2[index]]+=1
        
        if asDict==sliding:
            
                return True
            
        left=0
        for index in range(len(s1),len(s2)):
            sliding[s2[index]]+=1
            sliding[s2[left]]-=1
            if not sliding[s2[left]]:
                del sliding[s2[left]]
                
            left+=1
            if asDict==sliding:
            
                return True
        return False
        