from _heapq import heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        for i in range(len(points)):
            x1, x2 = points[i][0], points[i][1]
            distances[i] = [points[i], x1 ** 2 + x2 ** 2]
        
        heap = []
        for i in range(len(distances)):
            heapq.heappush(heap, [distances[i][1], distances[i][0]])
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
