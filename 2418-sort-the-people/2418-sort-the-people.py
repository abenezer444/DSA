class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for minIndex in range(len(names)):
            minindex=minIndex
            for num in range(minIndex+1,len(names)):
                if heights[minindex]<heights[num]:
                    minindex=num
                    minNum=heights[num]
            names[minIndex],names[minindex]=names[minindex],names[minIndex]
            heights[minIndex],heights[minindex]=heights[minindex],heights[minIndex]
                
                
        
                    
       
        return names
        