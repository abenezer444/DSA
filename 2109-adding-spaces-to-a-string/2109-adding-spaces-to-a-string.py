class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        resArr = []
        i = 0
        
		# Take portions of the string between spaces and put them in the list
        for index in spaces:
            portion = s[i:index]
            resArr.append(portion)
            i = index
            
        #Put the remaining string in resArr
        resArr.append(s[spaces[len(spaces) - 1]:])
        return " ".join(resArr)
        