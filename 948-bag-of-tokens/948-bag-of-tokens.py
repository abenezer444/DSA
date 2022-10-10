class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        l=0
        r=len(tokens)-1
        score=0
        temp=0
        while l<=r:
            while power>0 and l<len(tokens) and tokens[l]<=power:
                temp+=1
                power-=tokens[l]
                l+=1
            score=max(temp,score)
            if temp>0:
                power+=tokens[r]
                temp-=1
            r-=1
        return score
        