class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        operation={'+','-','/','*'}
        for i in tokens:
            if i in operation:
                if i=="+":
                    new=(stack[-2]+stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(new)
                if i=="-":
                    new=(stack[-2]-stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(new)
                if i=="*":
                    new=(stack[-2]*stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(new)
                if i=="/":
                    new=(int(float(stack[-2])/stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(new)
                    
            else:
                stack.append(int(i))
        return stack[0]
                
        