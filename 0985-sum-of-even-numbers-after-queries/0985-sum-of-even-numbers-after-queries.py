class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def isEven(val):
            return val%2==0
        ans=[]
        evenSum=0
        for num in nums:
            if num%2==0:
                evenSum+=num
        for i in range(len(queries)):
            query=queries[i]
            val,index=query[0],query[1]
            if isEven(val) and isEven(nums[index]):
                evenSum+=val
            elif (not isEven(val)) and (not isEven(nums[index])):
                evenSum+=nums[index]+val
            elif  (not isEven(val)) and isEven(nums[index]):
                evenSum-= nums[index]
            nums[index]+=val
            ans.append(evenSum)
        return ans
        
                
        