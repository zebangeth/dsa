class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        queue = collections.deque([0])
        farthest = 0
        while queue:
            cur = queue.popleft()
            for i in range(max(cur + minJump, farthest), min(cur + maxJump + 1, len(s))):
                if s[i] == '0':
                    queue.append(i)
                    farthest = max(i, farthest)
                    if i == len(s) - 1:
                        return True
        
        return False
