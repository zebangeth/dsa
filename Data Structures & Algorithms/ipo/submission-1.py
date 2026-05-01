class Solution:
    def findMaximizedCapital(
        self, 
        k: int, 
        w: int, 
        profits: List[int], 
        capital: List[int]
    ) -> int:
        requirements = collections.deque(
            sorted((capital[i], profits[i]) for i in range(len(profits)))
        )

        heap = []  # max heap by profit，用负数实现

        while k > 0:
            # 把当前资金 w 能启动的项目全部加入 heap
            while requirements and requirements[0][0] <= w:
                cap, profit = requirements.popleft()
                heapq.heappush(heap, -profit)

            # 如果没有任何可做项目，就提前结束
            if not heap:
                break

            # 选择 profit 最大的项目
            w += -heapq.heappop(heap)
            k -= 1

        return w