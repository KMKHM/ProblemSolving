"""
https://leetcode.com/problems/count-and-say/description/?envType=daily-question&envId=2025-04-18
"""

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        def recur(depth, cur):
            if depth == n:
                return cur

            string = cur[0]
            tmp = 0
            nex = ""
            for c in cur:
                if string == c:
                    tmp += 1
                else:
                    nex += (str(tmp) + string)
                    string = c
                    tmp = 1
            nex += (str(tmp) + string)
            return recur(depth + 1, nex)

        return recur(1, "1")