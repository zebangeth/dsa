class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suffix = [0] * (len(piles) + 1)
        for i in range(len(piles) - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        return self.dfs(piles, suffix, dict(), 0, 1)
        
    # the max stones current player can get from piles[i:]
    def dfs(self, piles, suffix, memo, i, m):
        if i == len(piles):
            return 0
        
        if (i, m) in memo:
            return memo[(i, m)]
        
        max_stones = 0

        for j in range(i, min(len(piles), i + 2 * m)):
            x = j - i + 1

            max_stones = max(
                max_stones,
                suffix[i] - self.dfs(piles, suffix, memo, j + 1, max(m, x))
            )
        
        memo[(i, m)] = max_stones
        return max_stones