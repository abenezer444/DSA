class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num-3)%3==0:
            root=(num-3)//3
        else:
            return []
        return [root,root+1,root+2]
        