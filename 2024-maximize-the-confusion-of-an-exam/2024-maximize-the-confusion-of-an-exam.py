class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        res=0
        l=0
        true=0
        false=0
        for r in range(len(answerKey)):
            if answerKey[r]=='T':
                true+=1
            else:
                false+=1
            if true>k and false>k:
                if answerKey[l]=='T':
                    true-=1
                else:
                    false-=1
                l+=1
            res=max(res,r-l+1)
        return res

                 


        