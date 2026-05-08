class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)

        # state: dp[i][j] stores weather s[i : j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        longest = 1
        li, lj = 0, 0

        # initialization
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest = 2
                li, lj = i, i + 1


        # function
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = 1
                    if j - i + 1 > longest:
                        longest = j - i + 1
                        li, lj = i, j
        
        return s[li : lj + 1]