class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pairs=collections.Counter(words)
        pair=[(-count,word) for (word,count) in pairs.items()]
        heapify(pair)
        res=[]
        for i in range(k):
            res.append(heappop(pair)[1])
        return res