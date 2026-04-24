class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([(str(len(s)) + "#" + s) for s in strs])

    def decode(self, s: str) -> List[str]:
        strs = []

        cur_str_len = 0
        i = 0
        while i < len(s):
            c = s[i] 
            if c.isdigit(): 
                cur_str_len = cur_str_len * 10 + int(c)
                i += 1
                continue
            if c == "#":
                strs.append(s[i+1 : i+cur_str_len+1])
                i = i + cur_str_len + 1
                cur_str_len = 0
                continue
        return strs

