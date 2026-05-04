class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.dfs(s, 0, [])
        return self.ans
    
    def dfs(self, s, start, result):
        if start == len(s):
            self.ans.append(result[:])
            return
        
        for i in range(start, len(s)):
            if not self.is_palindrome(s, start, i):
                continue
            self.dfs(s, i + 1, result + [s[start : i+1]])

    
    def is_palindrome(self, s, start, end):
        l, r = start, end
        while l <= r:
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1
        return True
