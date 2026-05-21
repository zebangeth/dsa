class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = [(-counter[c], c) for c in counter]
        heapq.heapify(heap)
        print
        cooldown = tuple() # (c, cnt)
        result = []
        while heap or cooldown:
            if not heap:
                return ""
            neg_cnt, cur_c = heapq.heappop(heap)
            result.append(cur_c)
            remain_cnt = -neg_cnt - 1
            if cooldown:
                c, cnt = cooldown
                heapq.heappush(heap, (-cnt, c))
                cooldown = tuple()
            if remain_cnt >= 1:
                cooldown = (cur_c, remain_cnt)
        
        return "".join(result)