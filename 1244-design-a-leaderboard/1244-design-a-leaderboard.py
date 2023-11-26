class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.front = Node(-1)
        self.rear = Node(-1)
        
        self.front.next, self.rear.prev = self.rear, self.front
    def show(self):
        nodes = []
        cur = self.front
        while cur:
            nodes.append(str(cur.val))
            cur = cur.next
        print('->'.join(nodes))
    def get_top_k(self, k):
      
        cur = self.front.next
        
        
        count = 0
        score = 0
        
        while count != k:
            
            score += cur.val
            cur = cur.next
            count += 1
        return score
    def add_node(self,node):
      
        
     
        if self.front.next == self.rear:
            self.front.next = node
            node.prev = self.front
            self.rear.prev = node
            node.next = self.rear
        else:
            cur = self.front.next
            
            while cur.val > node.val:
                cur = cur.next
                
            cur.prev.next = node
            node.prev = cur.prev
            node.next = cur
            cur.prev = node
    def update_node(self, node, new_node):
        #delete the node
      
     
        cur = self.front
        
        while cur and cur != node:
            
            cur = cur.next
        
        
        if cur:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

        #call add_node
      
        self.add_node(new_node)
        
        
            
            



class Leaderboard:

    def __init__(self):
        self.scoreboard = DoublyLinkedList()
        self.scores = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        
        if playerId in self.scores:
            old = self.scores[playerId]
            
            new = Node(score + old.val)
           
            self.scores[playerId] = new
            self.scoreboard.update_node(old, new)
        else:
            self.scores[playerId] = Node(score)
            self.scoreboard.add_node(self.scores[playerId])
        

    def top(self, K: int) -> int:
        return self.scoreboard.get_top_k(K)
        

    def reset(self, playerId: int) -> None:
        new = Node(0) 
        
        self.scoreboard.update_node(self.scores[playerId], new )
        self.scores[playerId] = new
        
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)