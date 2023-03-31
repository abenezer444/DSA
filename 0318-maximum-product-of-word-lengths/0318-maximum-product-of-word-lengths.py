class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        def getWordAsBit(word):
            bit = 0
            for char in word:
                bit |= 1 << ord(char)-ord('a')
            return bit
        wordsAsBit = [getWordAsBit(word) for word in words]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not (wordsAsBit[i] & wordsAsBit[j]):
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans
                    
    
            
        