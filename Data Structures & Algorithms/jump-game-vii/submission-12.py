class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        queue = collections.deque([0])
        farthest = 0
        while queue:
            cur = queue.popleft()
            if cur == len(s) - 1:
                return True
            start = max(farthest, cur + minJump)
            end = min(cur + maxJump, len(s) - 1)
            if start > end:
                continue
            for i in range(start, end + 1):
                if s[i] == '1':
                    continue
                queue.append(i)
            farthest = max(farthest, end)

        return False
                