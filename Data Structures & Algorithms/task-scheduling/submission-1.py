class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        heap = [-cnt for cnt in counter.values()]
        heapq.heapify(heap)
        cooldown = collections.deque()  # (available_time, remaining_count)
        time = 0

        while heap or cooldown:
            while cooldown and cooldown[0][0] <= time:
                heapq.heappush(heap, cooldown[0][1])
                cooldown.popleft()
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1
                if cnt < 0:
                    cooldown.append((time + n + 1, cnt))
            time += 1
        
        return time

