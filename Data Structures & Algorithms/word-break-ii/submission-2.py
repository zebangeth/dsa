class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.breaks = []
        self.dfs(s, 0, set(wordDict), [])
        return self.breaks
        

    def dfs(self, s, start, words, cur):
        if start == len(s):
            self.breaks.append(" ".join(cur))
            return
        
        for i in range(start, len(s)):
            if s[start : i + 1] in words:
                self.dfs(s, i + 1, words, cur + [s[start : i + 1]])
        
