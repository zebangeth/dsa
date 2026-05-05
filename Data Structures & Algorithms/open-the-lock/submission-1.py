class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        if "0000" in deads:
            return -1
        
        steps = 0
        queue = collections.deque(["0000"])
        visited = set(["0000"])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return steps
                for possible in self._rotate(deads, visited, cur):
                    queue.append(possible)
                    visited.add(possible)
            steps += 1
        return -1


    def _rotate(self, deads, visited, cur):
        """
        return all possible rotate results
        """
        possibles = set()
        for i, c in enumerate(cur):
            c_pre = str((int(c) + 9) % 10)
            c_nxt = str((int(c) + 1) % 10)
            cur_pre = cur[:i] + c_pre + cur[i + 1:]
            cur_nxt = cur[:i] + c_nxt + cur[i + 1:]
            possibles.add(cur_pre)
            possibles.add(cur_nxt)
        return possibles - deads - visited