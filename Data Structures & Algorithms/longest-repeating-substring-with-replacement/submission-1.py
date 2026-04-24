class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idea: sliding window
        # record the most freq c in the sliding window
        # if (size of the window - freq) >  k, the window size need to get smaller
        # track the largest window size and return that as the output
        longest = 0
        frq_dic = collections.defaultdict(int)
        max_frq = 0
        l, r = 0, 0

        while r < len(s):
            frq_dic[s[r]] += 1
            max_frq = max(max_frq, frq_dic[s[r]])

            # shrink the window if more than k chars in the window need to be replaced
            while r - l - max_frq + 1 > k:
                frq_dic[s[l]] -= 1
                # 这里不用更新 max_frq
                # 因为只有 max_frq 变得更大的时候才可能获得更长的重复子串
                l += 1

            longest = max(longest, r - l + 1)
            r += 1

        return longest
