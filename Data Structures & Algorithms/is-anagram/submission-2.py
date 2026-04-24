class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return collections.Counter(s) == collections.Counter(t)
        return self._counter(s) == self._counter(t)
    
    def _counter(self, seq):
        counter = dict()
        for x in seq:
            if x not in counter:
                counter[x] = 0
            counter[x] += 1
        return counter