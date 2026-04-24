class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        req = collections.Counter(t)
        had = collections.defaultdict(int)
        l = 0
        shortest_size = len(s)
        shortest_str_idx = []
        for r in range(len(s)):
            had[s[r]] += 1
            while l <= r and self.include_all(had, req):
                if r - l + 1 <= shortest_size:
                    shortest_size = r - l + 1
                    shortest_str_idx = [l, r + 1]
                had[s[l]] -= 1
                l += 1
        return "" if not shortest_str_idx else s[shortest_str_idx[0] : shortest_str_idx[1]]
            
    def include_all(self, had, req):
        for k in req:
            if req[k] > had[k]:
                return False
        return True
            