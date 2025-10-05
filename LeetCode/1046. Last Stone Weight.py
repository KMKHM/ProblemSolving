class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for s in stones:
            heapq.heappush(q, -s)

        while len(q) >= 2:
            x, y = -heapq.heappop(q), -heapq.heappop(q)
            if x != y:
                heapq.heappush(q, -(x - y))
        return -q[0] if q else 0