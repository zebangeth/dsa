class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        heap = []
        if a > 0:
            heap.append((-a, "a"))
        if b > 0:
            heap.append((-b, "b"))
        if c > 0:
            heap.append((-c, "c"))
        heapq.heapify(heap)
        cooldown = None
        idx = 0
        while heap:
            remain, char = heapq.heappop(heap)
            result.append(char)
            remain += 1
            if cooldown:
                heapq.heappush(heap, cooldown)
                cooldown = None
            if remain < 0 and len(result) >= 2 and result[-1] == result[-2]:
                cooldown = (remain, char)
            elif remain < 0:
                heapq.heappush(heap, (remain, char))
        return "".join(result)
