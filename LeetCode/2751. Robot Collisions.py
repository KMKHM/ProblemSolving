"""
2751. Robot Collisions
문제: https://leetcode.com/problems/robot-collisions/description/
"""
class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        stack = []

        for i in sorted(range(len(positions)), key=lambda i: positions[i]):
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[stack[-1]] < healths[i]:
                    healths[i] -= 1
                    healths[stack.pop()] = 0
                if stack:
                    if healths[stack[-1]] == healths[i]:
                        healths[stack.pop()] = 0
                    else:
                        healths[stack[-1]] -= 1
                    healths[i] = 0

        return [h for h in healths if h]