class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        longest = 0
        l, r = 0, 0
        for r in range(len(s)):
            while l < r and s[r] in unique:
                unique.remove(s[l])
                l += 1
            
            unique.add(s[r])
            longest = max(r - l + 1, longest)
        
        return longest
