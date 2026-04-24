class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        strs = []
        last = 0
        while last < len(s):
            # Find the position of '#' delimiter starting from 'last'
            num_c_pos = s.find("#", last)
            # Extract the length of the next string using the found position
            len_s = int(s[last:num_c_pos])
            word = s[num_c_pos + 1 : num_c_pos + 1 + len_s]
            strs.append(word)
            last = num_c_pos + 1 + len_s

        return strs