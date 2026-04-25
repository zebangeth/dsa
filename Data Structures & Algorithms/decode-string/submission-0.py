class Solution:
    def decodeString(self, s: str) -> str:
        result, _ = self._decode_part(s, 0)
        return result

    def _decode_part(self, s: str, i: int):
        result = []
        num = 0

        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)
                i += 1

            elif ch == '[':
                inner, i = self._decode_part(s, i + 1)
                result.append(inner * num)
                num = 0
                i += 1

            elif ch == ']':
                return ''.join(result), i

            else:
                result.append(ch)
                i += 1

        return ''.join(result), i
