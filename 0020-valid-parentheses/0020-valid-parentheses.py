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
        for i in s:
            if i in opening:
                stack.append(i)
            elif stack and pmap[i]==stack[-1]:
                stack.pop()
            else:
                return False
        return not bool(stack)
        