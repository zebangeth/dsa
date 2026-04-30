class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = [(-counter[char], char) for char in counter]
        heapq.heapify(heap)
        cooldown = None # (-cnt, char)
        result = []

        while heap or cooldown:
            if not heap:
                return ""
            cnt, char = heapq.heappop(heap)
            result.append(char)
            cnt += 1
            if cooldown and result[-1] != cooldown[1]:
                heapq.heappush(heap, cooldown)
                cooldown = None

            if cnt < 0:
                cooldown = (cnt, char)
        
        return "".join(result)

# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         counter = collections.Counter(s)
#         heap = [(-cnt, char) for char, cnt in counter.items()]
#         heapq.heapify(heap)

#         prev = None
#         result = []

#         while heap:
#             cnt, char = heapq.heappop(heap)
#             result.append(char)
#             cnt += 1

#             # 上一轮冷却的字符现在可以放回去了
#             if prev:
#                 heapq.heappush(heap, prev)

#             # 当前字符如果还剩，进入 cooldown
#             prev = (cnt, char) if cnt < 0 else None

#         return "" if prev else "".join(result)

