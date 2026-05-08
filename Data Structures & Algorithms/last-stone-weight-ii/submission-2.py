class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half = total // 2

        # state: dp[n][w] stores the max weight can get using stones[:n] <= w
        dp = [[0] * (half + 1) for _ in range(len(stones) + 1)]

        # initialization

        # state transition function
        for n in range(1, len(stones) + 1):
            for w in range(half + 1):
                if w >= stones[n - 1]:
                    # option 1: take the current stone
                    dp[n][w] = max(dp[n][w], stones[n - 1] + dp[n - 1][w - stones[n - 1]])
                # option 2: not take the current stone
                dp[n][w] = max(dp[n][w], dp[n - 1][w])

        print(dp)
        # answer
        return abs(dp[len(stones)][half] - (total - dp[len(stones)][half]))