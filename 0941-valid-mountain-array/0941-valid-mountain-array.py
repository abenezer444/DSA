class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        index = 0

       
        while index+1 < length and arr[index] < arr[index+1]:
            index += 1

       
        if index == 0 or index == length-1:
            return False

       
        while index+1 < length and arr[index] > arr[index+1]:
            index += 1

        return index == length-1