class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        cooldown = collections.deque() # [(cnt, nxt_available_time)]
        heap = [-counter[task] for task in counter]
        heapq.heapify(heap)
        time = 0

        while heap or cooldown:
            time += 1
            while cooldown and cooldown[0][1] < time:
                cnt, _ = cooldown.popleft()
                heapq.heappush(heap, -cnt)
            if heap:
                cnt = -heapq.heappop(heap)
                if cnt > 1:
                    cooldown.append((cnt - 1, time + n))
        
        return time
            

