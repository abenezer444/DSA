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
            for i in range(1,len(listDir)):
                text=(listDir[0]+'/'+listDir[i][:files(listDir[i])])
                file=listDir[i][files(listDir[i])+1:-1]
                fileMap[file].append(text)
        for item in fileMap.values():
            if len(item)>1:
                ans.append(item)
        return ans
       
                
                
                
                
                
            
        