class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) > i and s[i] == strs[0][i]:
                    continue
                return s[:i]
        # All s in strs are identical
        return strs[0]
