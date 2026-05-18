class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.extend([str(len(s)), '#', s])
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        cur_len = 0
        strs = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                cur_len = 10 * cur_len + int(c)
                i += 1
            elif c == '#':
                strs.append(s[i+1 : i+1+cur_len])
                i = i+1+cur_len
                cur_len = 0
            else:
                raise RuntimeError("Invalide encoding")
        
        return strs
