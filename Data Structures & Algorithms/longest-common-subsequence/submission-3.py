class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # state: dp[i][j] stores the LCS between text1[:i] and text2[:j]
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # transition function
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[len(text1)][len(text2)]
