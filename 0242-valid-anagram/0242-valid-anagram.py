class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count_s = [0]*26
        char_count_t = [0]*26
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            char_count_s[ord(char_s) - ord('a')] += 1
            char_count_t[ord(char_t) - ord('a')] += 1
        return char_count_s == char_count_t
            
            
        
    
        