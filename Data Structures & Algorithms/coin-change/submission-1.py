class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state: dp[i] stores the min number of coins to get amount i
        dp = [float("inf")] * (amount + 1)

        # initialization:
        dp[0] = 0

        # function:
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i - coin] + 1, dp[i])

        return dp[amount] if dp[amount] != float("inf") else -1