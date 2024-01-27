"""
Integer to Roman
문제: https://leetcode.com/problems/integer-to-roman/description/
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            "M": 1000, "CM": 900,
            "D": 500, "CD": 400,
            "C": 100, "XC": 90,
            "L": 50, "XL": 40,
            "X": 10, "IX": 9,
            "V": 5, "IV": 4,
            "I": 1
        }

        ans = ""

        while num != 0:
            for i, j in dic.items():
                if num - j >= 0:
                    num -= j
                    ans += i
                    break
        return ans

