class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # dp[i][0] stores the longest turbulence subarray ends with arr[i] as wave low
        # dp[i][1] stores the longest turbulence subarray ends with arr[i] as wave high
        dp = [[1] * len(arr) for _ in range(2)]

        # function
        for i in range(1, len(arr)):
            dp[0][i] = 1 + dp[1][i - 1] if arr[i] > arr[i - 1] else 1
            dp[1][i] = 1 + dp[0][i - 1] if arr[i] < arr[i - 1] else 1
        
        return max(max(dp[0]), max(dp[1]))
