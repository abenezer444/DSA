class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        tb={}
        res=20000000
        for idx,num in enumerate(cards):
            if num in tb:
                res=min(idx-tb[num]+1,res)
                tb[num]=idx
            else: tb[num]=idx
        if res==20000000:
            return -1
        return res
        