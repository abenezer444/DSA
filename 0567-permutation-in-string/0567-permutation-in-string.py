class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        asDict=Counter(s1)
        for index in range(len(s2)):
            if asDict==Counter(s2[index:index+len(s1)]):
                return True
        return False
        