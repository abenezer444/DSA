class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        minLen=float('inf')
        cardMap={}
        for idx,card in enumerate(cards):
            if card in cardMap:
                minLen=min(minLen,idx-cardMap[card]+1)
            cardMap[card]=idx
        if minLen==float('inf'):
            return -1
        return minLen
    
