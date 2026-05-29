class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        return self.dfs(s, 0, 0, memo)

    def dfs(self, s, i, balance, memo):
        # 右括号太多，非法
        if balance < 0:
            return False

        if (i, balance) in memo:
            return memo[(i, balance)]

        if i == len(s):
            return balance == 0

        if s[i] == '(':
            res = self.dfs(s, i + 1, balance + 1, memo)

        elif s[i] == ')':
            res = self.dfs(s, i + 1, balance - 1, memo)

        else:  # s[i] == '*'
            res = (
                self.dfs(s, i + 1, balance + 1, memo) or  # treat as '('
                self.dfs(s, i + 1, balance - 1, memo) or  # treat as ')'
                self.dfs(s, i + 1, balance, memo)         # treat as empty
            )

        memo[(i, balance)] = res
        return res