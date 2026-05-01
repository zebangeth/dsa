class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        self.dfs(n, n, [])
        return self.results
        
    def dfs(self, lp, rp, result):
        if lp == rp == 0:
            self.results.append("".join(result))
            return
        
        if lp > 0:
            self.dfs(lp - 1, rp, result + ['('])
        if rp > lp:
            self.dfs(lp, rp - 1, result + [')'])