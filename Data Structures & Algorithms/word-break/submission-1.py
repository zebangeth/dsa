class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] stores if word[:i] is breakable
        dp = [False] * (len(s) + 1)

        # initialization
        dp[0] = True

        # function
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if len(word) > i:
                    continue

                if dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break

        return dp[-1]