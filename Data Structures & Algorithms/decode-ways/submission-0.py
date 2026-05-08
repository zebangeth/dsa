class Solution:
    def numDecodings(self, s: str) -> int:
        memo = dict()
        return self.dfs(s, 0, memo)

    def dfs(self, s, start, memo):
        if start in memo:
            return memo[start]

        if start == len(s):
            return 1
        
        if s[start] == '0':
            return 0
        
        count = self.dfs(s, start + 1, memo)

        if start + 1 < len(s) and int(s[start:start + 2]) <= 26:
            count += self.dfs(s, start + 2, memo)
        
        memo[start] = count
        return count