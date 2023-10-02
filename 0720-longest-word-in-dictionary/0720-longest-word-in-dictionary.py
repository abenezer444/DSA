class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertWord(self,word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True
    def isPossible(self,word):
        cur = self.root
        for char in word:
            if not cur.children[char].end:
                return False
            cur = cur.children[char]
        return True
            
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        ans = ''
        
        for word in words:
            trie.insertWord(word)
        for word in words:
            if trie.isPossible(word):
                if len(word) == len(ans) and word < ans:
                    ans = word
                    
                if len(word) > len(ans):
                    ans = word
        return ans
                
        