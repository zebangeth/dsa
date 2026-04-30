class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [[(x ** 2 + y ** 2) ** 0.5, x, y] for (x, y) in points]
        heapq.heapify(distance)
        result = []

        for _ in range(k):
            d, x, y = heapq.heappop(distance)
            result.append([x, y])
        return result

            