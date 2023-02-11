class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        idx=0
        players = [playerNum+1 for playerNum in range(n)] 
        while len(players)>1:
            idx = (idx+k-1) % len(players) 
            players.pop(idx) 
        return players[0]
        