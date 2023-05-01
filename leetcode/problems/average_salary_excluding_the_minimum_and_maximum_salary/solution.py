class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        val = len(salary)
        return sum(salary[1:len(salary)-1])/(val-2)