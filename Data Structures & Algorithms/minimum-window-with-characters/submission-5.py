class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req = collections.Counter(t)
        had = collections.defaultdict(int)

        remain = len(req)  # 还有多少种字符没有满足
        min_len = float("inf")
        min_str = ""

        l = 0

        for r in range(len(s)):
            c = s[r]

            # expand right
            if c in req:
                had[c] += 1
                if had[c] == req[c]:
                    remain -= 1

            # shrink left while valid
            while remain == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_str = s[l:r + 1]

                left_char = s[l]
                if left_char in req:
                    had[left_char] -= 1

                    # removing this char makes the window invalid
                    if had[left_char] < req[left_char]:
                        remain += 1

                l += 1

        return min_str