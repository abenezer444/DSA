class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        pair=[(heights[i],names[i]) for i in range(len(names))]
        for i in range(len(pair)):
            for j in range(len(pair)-1):
                if pair[j]<pair[j+1]:
                    pair[j],pair[j+1]=pair[j+1],pair[j]
        ans=[]
        for num in pair:
            ans.append(num[1])
        return ans
        