class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        queue = collections.deque([0])
        visited = set([0])
        while queue:
            cur = queue.popleft()
            for i in range(cur + minJump, min(cur + maxJump + 1, len(s))):
                if i in visited:
                    continue
                if s[i] == '0':
                    queue.append(i)
                    visited.add(i)
                    if i == len(s) - 1:
                        return True
        
        return False
