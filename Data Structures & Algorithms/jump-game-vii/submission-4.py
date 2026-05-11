class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        queue = collections.deque([0])
        farthest = 0

        while queue:
            cur = queue.popleft()

            start = max(cur + minJump, farthest + 1)
            end = min(cur + maxJump, n - 1)

            for i in range(start, end + 1):
                if s[i] == '0':
                    if i == n - 1:
                        return True
                    queue.append(i)

            farthest = max(farthest, end)

        return n == 1