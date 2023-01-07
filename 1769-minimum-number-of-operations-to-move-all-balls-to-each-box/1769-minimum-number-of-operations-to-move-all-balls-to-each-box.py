class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[0]*len(boxes)
        for idx,box in enumerate(boxes):
            ops=0
            for index in range(len(boxes)):
                if index!=idx and boxes[index]=='1':
                    ops+=abs(idx-index)
            ans[idx]=ops
                    
        
        
        return ans