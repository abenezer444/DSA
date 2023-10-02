class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 1
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            else:
                cur.children[char].count += 1
            cur = cur.children[char]
    def score(self,word):
        cur = self.root
        total = 0
        for char in word:
            total += cur.children[char].count
            cur = cur.children[char]
        return total
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            ans.append(trie.score(word))
        return ans
        