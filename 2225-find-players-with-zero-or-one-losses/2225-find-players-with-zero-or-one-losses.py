class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans0=[]
        ans1=[]
        winners=set()
        lossers={}
        for match in matches:
            winners.add(match[0])
            lossers[match[1]]=1+lossers.get(match[1],0)
        for winner in winners:
            if winner not in lossers:
                ans0.append(winner)
        for losser in lossers:
            if lossers[losser]==1:
                ans1.append(losser)
        ans0.sort()
        ans1.sort()
        answer=[ans0,ans1]
        
            
        return answer
            
        