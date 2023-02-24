class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        opening={'(','[','{'}
        #add openings to the stack
        #if not opening, check if current punc value and the end of the stack are the same
        #if not same return false
        #else pop stack
        pmap={')':'(',']':'[','}':'{'}
        for mark in s:
            if mark in opening:
                stack.append(mark)
            elif stack and pmap[mark]==stack[-1]:
                stack.pop()
            else:
                return False
        return not (stack)
        