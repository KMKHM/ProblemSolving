"""
문제: https://leetcode.com/problems/finding-3-digit-even-numbers
"""
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res=set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i==j:
                    continue
                for k in range(n):
                    if digits[k] % 2 or j == k or k == i:
                        continue
                    res.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return sorted(res)