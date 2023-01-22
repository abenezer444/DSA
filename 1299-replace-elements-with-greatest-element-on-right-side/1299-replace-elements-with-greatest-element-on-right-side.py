class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp=-1
        for index in range(len(arr)-1,-1,-1):
            arr[index],temp=temp,max(temp,arr[index])
        return arr
        