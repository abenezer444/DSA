class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def recur(i):
            maxx = 0
            if i >= len(questions):
                return maxx
            
            solve = questions[i][0] + recur(i + questions[i][1] + 1)
            notSolve = recur(i+1)
            
            maxx += max(solve,notSolve)
            return maxx
        return recur(0)
        