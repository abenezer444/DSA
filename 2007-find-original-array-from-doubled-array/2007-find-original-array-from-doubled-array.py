class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed)%2 or not changed:
            return []
        changed.sort()
        result=[]
        count=Counter(changed)
        for num in changed:
            if num and count[num] and count[2*num]:
                result.append(num)
                count[num]-=1
                count[2*num]-=1
            elif num==0 and count[num] and count[num]>1:
                result.append(num)
                count[num]-=2
        if len(result)==len(changed)/2:
            return result
        return []
                
                
                
        
        