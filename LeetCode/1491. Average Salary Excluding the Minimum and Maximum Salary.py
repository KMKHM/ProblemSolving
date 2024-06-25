"""
Average Salary Excluding the Minimum and Maximum Salary
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""

class Solution:
    def average(self, salary):
        salary.sort()
        return sum(salary[i] for i in range(1, len(salary)-1)) / (len(salary) - 2)