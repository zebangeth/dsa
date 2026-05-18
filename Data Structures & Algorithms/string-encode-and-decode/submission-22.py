class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.extend([str(len(s)), '#', s])
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            nxt_delimiter = s.find('#', i)
            str_len = int(s[i:nxt_delimiter])
            strs.append(s[nxt_delimiter + 1 : nxt_delimiter + 1 + str_len])
            i = nxt_delimiter + 1 + str_len
        
        return strs
