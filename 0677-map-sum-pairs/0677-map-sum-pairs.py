class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0
class MapSum(object):
    

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        cur = self.root
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.value = val
        
    def compute(self,node): 
        total = node.value
        for child in node.children.keys():
            total += self.compute(node.children[child])
        return total
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]

        return self.compute(cur) 
        
