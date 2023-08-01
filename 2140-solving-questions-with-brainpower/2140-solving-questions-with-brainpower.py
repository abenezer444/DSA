class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def recur(i):
            maxx = 0
            if i in memo:
                return memo[i]
            if i >= len(questions):
                return maxx
            
            solve = questions[i][0] + recur(i + questions[i][1] + 1)
            notSolve = recur(i+1)
            
            maxx += max(solve,notSolve)
            memo[i] = maxx
            return memo[i]
        return recur(0)
        