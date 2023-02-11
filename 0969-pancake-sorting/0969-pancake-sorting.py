class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        number=len(arr)
        def findNum(number):
            for idx,num in enumerate(arr):
                if num==number:
                    return idx
                
            
        def flip(index):
            left=0
            while left<index:
                arr[left],arr[index]=arr[index],arr[left]
                left+=1
                index-=1
        for num in range(number,1,-1):
            ans.append(findNum(num)+1)
            ans.append(num)
            flip(findNum(num))
            flip(num-1)
        return ans
        
            