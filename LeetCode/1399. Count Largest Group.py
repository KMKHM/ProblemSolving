"""
1399. Count Largest Group
문제: https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23
"""
from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:

        def transform(num):
            val = 0
            while num:
                val += num % 10
                num //= 10
            return val

        dic = Counter()
        max_len = 0

        for num in range(1, n + 1):
            val = transform(num)
            dic[val] += 1
            max_len = max(max_len, dic[val])

        return sum(1 for i in dic.values() if i == max_len)