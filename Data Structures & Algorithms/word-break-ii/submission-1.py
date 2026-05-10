class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.breaks = []
        self.dfs(s, 0, set(wordDict), [])
        return self.breaks
        

    def dfs(self, s, start, words, cur):
        if start == len(s):
            self.breaks.append(" ".join(cur))
            return
        
        for i in range(start + 1, len(s) + 1):
            if s[start : i] in words:
                self.dfs(s, i, words, cur + [s[start : i]])
        
