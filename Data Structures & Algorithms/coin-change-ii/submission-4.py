class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        # state: dp[i][j] stores the number of comb to amount i using coins[:j]
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]

        # initialization
        for j in range(len(coins) + 1):
            dp[0][j] = 1

        # state transition
        for i in range(1, amount + 1):
            for j in range(1, len(coins) + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - coins[j - 1]][j]

        return dp[amount][len(coins)]
