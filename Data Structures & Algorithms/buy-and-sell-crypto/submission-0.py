class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1: O(n) time, O(n) space
        pre_low = [float("inf")] * len(prices)
        for i in range(1, len(prices)):
            pre_low[i] = min(pre_low[i - 1], prices[i - 1])

        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - pre_low[i])
        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1 (optimized): O(n) time, O(1) space
        prev_min = float("inf")
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - prev_min)
            if price < prev_min:
                prev_min = price
        return max_profit
