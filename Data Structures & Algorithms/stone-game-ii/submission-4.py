class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = dict()
        return self.dfs(piles, memo, True, 0, 1)
    
    def dfs(self, piles, memo, alice, i, m):
        if i >= len(piles):
            return 0
        
        if (alice, i, m) in memo:
            return memo[(alice, i, m)]
        
        alice_stones = 0 if alice else float("inf")
        for x in range(1, 2 * m + 1):
            if i + x > len(piles):
                break
            if alice:
                alice_stones = max(
                    alice_stones, 
                    sum(piles[i:i+x]) + self.dfs(piles, memo, False, i + x, max(x, m))
                )
            else:
                alice_stones = min(
                    alice_stones, 
                    self.dfs(piles, memo, True, i + x, max(x, m))
                )
        memo[(alice, i, m)] = alice_stones
        return alice_stones
