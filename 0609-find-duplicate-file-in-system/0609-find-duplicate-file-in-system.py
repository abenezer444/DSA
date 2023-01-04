class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans=[]
        fileMap=defaultdict(list)
        
        def files(text):
            
            for idx,char in enumerate(text):
                
                if char=='(':
                    
                    return idx
        for dirr in paths:
            
            listDir=dirr.split()
            
            for position in range(1,len(listDir)):
                
                index=files(listDir[position])
                directory=(listDir[0]+'/'+listDir[position][:index])
                file=listDir[position][index+1:-1]
                fileMap[file].append(directory)
                
        for item in fileMap.values():
            
            if len(item)>1:
                
                ans.append(item)
                
        return ans
       
                
                
                
                
                
            
        