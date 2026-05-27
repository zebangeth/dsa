class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 0
        max_str = ""
        for i in range(len(s) - 1):
            odd_len, odd_str = self.find_longest(s, i, i)
            even_len, even_str = self.find_longest(s, i, i + 1)
            if odd_len > max_len:
                max_len = odd_len
                max_str = odd_str
            if even_len > max_len:
                max_len = even_len
                max_str = even_str
        return max_str
    
    def find_longest(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            j += 1
            i -= 1
        return j - i - 1, s[i + 1:j]
