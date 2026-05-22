class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.results = []
        self.dfs(s, [], 0)
        return self.results

    def dfs(self, s, result, start):
        if start == len(s):
            self.results.append(list(result))
            return
        
        for i in range(start, len(s)):
            if self.is_palindrome(s, start, i):
                result.append(s[start : i+1])
                self.dfs(s, result, i + 1)
                result.pop()
            
        
    def is_palindrome(self, s, start, end):
        while start < end:
            if not s[start] == s[end]:
                return False
            start += 1
            end -= 1
        return True