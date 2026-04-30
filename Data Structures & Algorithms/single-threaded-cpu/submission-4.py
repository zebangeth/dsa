class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        can_process = []
        heapq.heapify(can_process)
        need_process = [(enq, pro, idx) for idx, (enq, pro) in enumerate(tasks)]
        need_process.sort(reverse=True)
        time = 0
        
        result = []
        while can_process or need_process:
            while need_process and need_process[-1][0] <= time:
                heapq.heappush(can_process, (need_process[-1][1], need_process[-1][2]))
                need_process.pop()
            if can_process:
                process_time, idx = heapq.heappop(can_process)
                result.append(idx)
                time += process_time
            else:
                time = need_process[-1][0]

        return result