class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        max_frq = 0
        frq_dict = collections.defaultdict(int)
        l, r = 0, 0

        for r in range(len(s)):
            frq_dict[s[r]] += 1
            max_frq = max(max_frq, frq_dict[s[r]])
            while r - l + 1 > max_frq + k:
                frq_dict[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        
        return longest
