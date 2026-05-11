class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = collections.Counter(s)

        substrings = []
        i = 0
        substring_start = 0
        while i < len(s):
            substring_chars = set([s[i]])
            while substring_chars:
                counter[s[i]] -= 1
                if s[i] not in substring_chars:
                    substring_chars.add(s[i])
                if counter[s[i]] == 0:
                    substring_chars.remove(s[i])
                i += 1
            substrings.append(i - substring_start)
            substring_start = i
        return substrings
