class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        res = ""
        for s in strs: 
            res = res + str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:        
        res = []
        l = 0
        i = 0
        while i < len(s): 
            while s[i].isdigit(): 
                l = l * 10 + int(s[i])
                i += 1
            end = l + i
            res.append(s[i + 1 : end + 1])
            l = 0
            i = end + 1
        
        return res
                    

        
