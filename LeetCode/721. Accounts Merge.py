"""
Accounts Merge
문제: https://leetcode.com/problems/accounts-merge/description/
"""

from collections import defaultdict, Counter
class Solution:
    def accountsMerge(self, accounts):

        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])

        def union(a, b):
            a, b = find(a), find(b)
            if a > b:
                parent[b] = a
            else:
                parent[a] = b

        parent = Counter()
        tmp = Counter()

        for elem in accounts:
            for i in elem[1:]:
                parent[i] = i
                tmp[i] = elem[0]

        for elem in accounts:
            for i in range(1, len(elem) - 1):
                for j in range(i + 1, len(elem)):
                    union(elem[i], elem[j])

        answer = defaultdict(list)
        for k, v in parent.items():
            answer[find(k)].append(k)

        res = []

        for k, v in answer.items():
            res.append([tmp[k]] + sorted(v))

        return res

