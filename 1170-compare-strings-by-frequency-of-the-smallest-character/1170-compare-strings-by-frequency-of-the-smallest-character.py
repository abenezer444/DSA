class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def findFreqOfMin(string):
            freqMap = Counter(string)
            minn = string[0]
            for char in string:
                minn = min(minn,char)
            return freqMap[minn]
        queries = [findFreqOfMin(query) for query in queries]
        words = [findFreqOfMin(word) for word in words]
        words.sort()
        ans = []
        for query in queries:
            ans.append(len(words)-bisect_right(words,query,0,len(words)))
        return ans
            
    
            
        