class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        slist=[ i for i in s ]
        tlist=[ i for i in t ]
        for letter in slist:
            tlist.remove(letter)
        return tlist[0]
        