class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freqMap = Counter(s)
        stack = []
        for char in s:
            if char in stack:
                freqMap[char] -= 1
                continue
            while stack and stack[-1]>=char and freqMap[stack[-1]] > 1:
                removed = stack.pop()
                freqMap[removed] -= 1
            
            stack.append(char)
                
                
        return "".join(stack)