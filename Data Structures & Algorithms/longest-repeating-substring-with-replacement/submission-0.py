class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idea: sliding window
        # record the most freq c in the sliding window
        # if (size of the window - freq) >  k, the window size need to get smaller
        # track the largest window size and return that as the output

        if len(s) <= k or len(s) == 0:
            return len(s)

        freq = 0
        freq_c = ""
        window = defaultdict(int)

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] > freq:
                freq = window[s[r]]
                freq_c = s[r]
            
            while l < r and r - l + 1 - freq > k:
                window[s[l]] -= 1
                l += 1
        return r - l + 1


