class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = [[point, (point[0]**2 + point[1]**2) ** 0.5] for point in points]
        arr.sort(key=lambda x:x[1])
        return [e[0] for e in arr[:k]]