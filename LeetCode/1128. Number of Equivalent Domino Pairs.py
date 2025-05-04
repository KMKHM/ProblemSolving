"""
문제: https://leetcode.com/problems/number-of-equivalent-domino-pairs
"""
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        dic = Counter()

        for d in dominoes:
            i, j = sorted(d)
            dic[(i, j)] += 1
        res=0
        for v in dic.values():
            if v > 1:
                res += (v * (v-1)) // 2

        return res