"""
Find Center of Star Graph
문제: https://leetcode.com/problems/find-center-of-star-graph/description/
"""
class Solution:
    def findCenter(self, edges):
        # 모든 노드가 연결되어 있으므로 앞에만 보면 된다.
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]