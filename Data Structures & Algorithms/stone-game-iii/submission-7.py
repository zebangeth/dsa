import sys

sys.setrecursionlimit(10**6)

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        optimal = self.dfs(0, stoneValue, dict())
        if optimal == 0:
            return "Tie"
        return "Alice" if optimal > 0 else "Bob"
        
    def dfs(self, start, stones, memo):
        if start >= len(stones):
            return 0
        
        if start in memo:
            return memo[start]
        
        optimal = float("-inf")
        take = 0
        for k in range(3):
            if k + start >= len(stones):
                break
            take += stones[start + k]
            optimal = max(optimal, take - self.dfs(start + k + 1, stones, memo))
        memo[start] = optimal
        return optimal
