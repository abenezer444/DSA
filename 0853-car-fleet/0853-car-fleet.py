class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        posSped=[]
        for i in range(len(position)):
            posSped.append([position[i],speed[i]])
        posSped.sort(reverse=True,key=lambda i:i[0])
        stack=[]
        for i in posSped:
            time=(float(target-i[0]))/float((i[1]))
            stack.append(time)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        
            
        return len(stack)
        