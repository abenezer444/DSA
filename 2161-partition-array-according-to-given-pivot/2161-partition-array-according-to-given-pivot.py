class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        numsLess=[]
        numsGreat=[]
        pivots=0
        for num in nums:
            if num<pivot:
                numsLess.append(num)
            elif num>pivot:
                numsGreat.append(num)
            else:
                pivots+=1
        pivots=[pivot]*pivots
        numsLess.extend(pivots)
        numsLess.extend(numsGreat)
        return numsLess
        