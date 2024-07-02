"""
Letter Combinations of a Phone Number
문제: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution:
    def letterCombinations(self, digits):
        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []

        n = len(digits)

        res = []

        def backtracking(level, char):
            if level == n:
                res.append(char)
                return

            string = nums[digits[level]]

            for s in string:
                backtracking(level + 1, char + s)

        backtracking(0, "")
        return res