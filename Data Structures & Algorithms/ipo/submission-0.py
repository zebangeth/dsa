class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        requirements = collections.deque(
            sorted([(capital[i], profits[i]) for i in range(len(profits))])
        )
        heap = []
        while requirements and requirements[0][0] <= w:
            heapq.heappush(heap, -requirements[0][1])
            requirements.popleft()
        
        total_profit = w
        while heap and k > 0:
            total_profit += -heapq.heappop(heap)
            k -= 1
            while requirements and requirements[0][0] <= total_profit:
                heapq.heappush(heap, -requirements[0][1])
                requirements.popleft()
        return total_profit
