class Solution:
    def average(self, salary):
        total = sum(salary)
        minimum = min(salary)
        maximum = max(salary)

        return (total - minimum - maximum) / (len(salary) - 2)