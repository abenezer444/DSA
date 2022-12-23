class Solution:
    def average(self, salary: List[int]) -> float:
        minimum=min(salary)
        maximum=max(salary)
        ans=(sum(salary)-(minimum+maximum))/(len(salary)-2)
        return ans
        