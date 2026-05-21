class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        cooldown = collections.deque() # (nxt_available, task, cnt)
        heap = [(-counter[task], task) for task in counter]  # (-cnt, task)
        print(heap)
        heapq.heapify(heap)
        time = 0
        while heap or cooldown:
            while cooldown and cooldown[0][0] <= time:
                nxt_available, task, cnt = cooldown.popleft()
                heapq.heappush(heap, (-cnt, task))
            if heap:
                neg_cnt, task = heapq.heappop(heap)
                if -neg_cnt - 1 > 0:
                    cooldown.append((time + n + 1, task, -neg_cnt - 1))
            time += 1
        return time

