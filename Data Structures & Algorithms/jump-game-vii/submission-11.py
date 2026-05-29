class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        queue = collections.deque([0])
        visited = set([0])
        while queue:
            cur = queue.popleft()
            if cur == len(s) - 1:
                return True
            for j in range(minJump, maxJump + 1):
                if cur + j in visited:
                    continue
                if cur + j >= len(s) or s[cur + j] == '1':
                    continue
                queue.append(cur + j)
                visited.add(cur + j)
        return False
                