class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numsMap={nums[i]:i for i in range(len(nums))}
        for ops in operations:
            index=numsMap[ops[0]]
            nums[index]=ops[1]
            numsMap[ops[1]]=index
        return nums