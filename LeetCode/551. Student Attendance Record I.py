"""
Student Attendance Record I
문제: https://leetcode.com/problems/student-attendance-record-i/
"""


class Solution:
    def checkRecord(self, s):
        return s.count("A") < 2 and s.count("LLL") < 1
