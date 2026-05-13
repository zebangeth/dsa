roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        ints = [roman[c] for c in s] + [0]
        res = 0
        for i in range(len(ints) - 1):
            if ints[i] < ints[i + 1]:
                res -= ints[i]
            else:
                res += ints[i]
        return res