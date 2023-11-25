class TrieNode:
    def __init__(self):
        self.children = {}
        self.top_three = defaultdict(int)
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert_word(self, word, count):
     
        cur = self.root
        
        for char in word:
       
            
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
     
            if word not in cur.top_three:
                cur.top_three[word] = -count
            else:
                cur.top_three[word] -= 1
          
            
              
    def top_three_(self, prefix):
      
        cur = self.root
        for char in prefix:
            
            if char not in cur.children:
                return []
            cur = cur.children[char]
       
        top_three_items = list(cur.top_three.items())
        top_three_items_r = [[count,word] for word, count in top_three_items]
        top_three_items_r.sort()
        
        # print(top_three_items_r,prefix,'++++',cur.top_three)
    
        top_three_words = []
        for count, word in top_three_items_r[:3]:
            top_three_words.append(word)
        # print(top_three_words)
      
        return top_three_words
        
    
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.key_word = []
        self.trie = Trie()
  
 
        for count, sentence in zip(times,sentences):
            self.trie.insert_word(sentence, count) 
       
        

    def input(self, c: str) -> List[str]:
       
        if c == '#':
        
            
            inputs = ''.join(self.key_word)
            
            
            self.trie.insert_word(inputs, 1)
            
            
            self.key_word = []
            return []
        else:
            
            self.key_word.append(c)
           
            inputs = ''.join(self.key_word)
#             print("********",inputs,"*********")
          
            
            return self.trie.top_three_(inputs)
        
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)