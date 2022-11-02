class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        minLen=len(cards)+1
        cardMap={}
        for idx,card in enumerate(cards):
            if card in cardMap:
                minLen=min(minLen,idx-cardMap[card]+1)
            cardMap[card]=idx
        if minLen>len(cards):
            return -1
        return minLen
    
