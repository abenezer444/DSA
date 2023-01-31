class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        chemistry=0
        totalskill=skill[right]+skill[left]
        print(skill)
        while left<right:
            if skill[right]+skill[left]==totalskill:
                chemistry+=skill[right]*skill[left]
                right-=1
                left+=1
            else:
                return -1
        return chemistry