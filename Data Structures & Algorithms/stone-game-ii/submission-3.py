class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suffix = [0] * (len(piles) + 1)
        for i in range(len(piles) - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        memo = dict()
        return self.dfs(piles, suffix, memo, 0, 1)
        
    # the max stones current player can get from piles[i:]
    def dfs(self, piles, suffix, memo, i, m):
        if i >= len(piles):
            return 0
        
        if (i, m) in memo:
            return memo[(i, m)]

        # if i + 2 * m >= len(piles):
        #     return suffix[i]

        max_score = 0
        for x in range(1, 2 * m + 1):
            if i + x > len(piles):
                break
            taken = suffix[i] - suffix[i + x]
            opponent_score = self.dfs(piles, suffix, memo, i + x, max(m, x))
            current_score = taken + (suffix[i + x] - opponent_score)
            max_score = max(max_score, current_score)
        memo[(i, m)] = max_score
        return max_score
