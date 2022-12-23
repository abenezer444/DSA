class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        small=min(len(word1),len(word2))
        large=max(len(word1),len(word2))
        ans=""
        for i in range(small):
            ans+=word1[i]
            ans+=word2[i]
        if large==len(word1) and large!=small:
            ans+=word1[small:]
        else:
            ans+=word2[small:]
        return ans
            
        