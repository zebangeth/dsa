class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_str = ""
        min_len = float('inf')
        req = collections.Counter(t)
        had = collections.defaultdict(int)
        remain = len(req)
        l, r = 0, 0
        while r < len(s):
            while r < len(s) and remain > 0:
                if s[r] in req:
                    had[s[r]] += 1
                    if had[s[r]] == req[s[r]]:
                        remain -= 1
                r += 1

            if remain > 0:
                return min_str
            while l < r:
                if s[l] not in req:
                    l += 1
                elif had[s[l]] > req[s[l]]:
                    had[s[l]] -= 1
                    l += 1
                else:
                    break
                
            if r - l < min_len:
                min_len = r - l
                min_str = s[l:r]
            # Move l forward by one to force the next search to find a new window.
            # If s[l] was required, this makes the current window invalid again,
            # so the outer loop will expand r until validity is restored.
            if s[l] in req:
                had[s[l]] -= 1
                if had[s[l]] < req[s[l]]:
                    remain += 1
            l += 1
        return min_str
