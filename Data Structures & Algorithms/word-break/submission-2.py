class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # state: dp[i] stores if dp[:i] is breakable
        dp = [False] * (len(s) + 1)

        # initialization
        dp[0] = True

        word_set = set(wordDict)
        for i in range(1, len(s) + 1):
            for word in word_set:
                if len(word) > i or s[i-len(word):i] != word:
                    continue
                if dp[i-len(word)]:
                    dp[i] = True
                    break
        print(dp)
        return dp[len(s)]