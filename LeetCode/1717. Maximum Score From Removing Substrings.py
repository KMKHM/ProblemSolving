"""
1717. Maximum Score From Removing Substrings
문제: https://leetcode.com/problems/maximum-score-from-removing-substrings/description/
"""


class Solution:
    def maximumGain(self, s, x, y):

        def operation(val1, val2, s1, s2, s):
            ans = 0
            stack = []
            for c in s:
                if stack and stack[-1] == s1 and c == s2:
                    ans += val1
                    stack.pop()
                else:
                    stack.append(c)
            s = "".join(stack)
            stack = []
            for c in s:
                if stack and stack[-1] == s2 and c == s1:
                    ans += val2
                    stack.pop()
                else:
                    stack.append(c)
            return ans

        return operation(x, y, "a", "b", s) if x >= y else operation(y, x, "b", "a", s)