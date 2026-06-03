class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] stores the num of ways to get to amount i using coins[:j]
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]

        # initialization
        for j in range(len(coins) + 1):
            dp[0][j] = 1

        coins.sort()
        # state transition
        for i in range(1, amount + 1):
            for j in range(1, len(coins) + 1):
                if coins[j - 1] > i:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - coins[j - 1]][j]
        # answer:
        return dp[amount][len(coins)]