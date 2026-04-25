class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                parts = []

                while stack[-1] != "[":
                    parts.append(stack.pop())

                stack.pop()

                parts.reverse()
                substr = "".join(parts)

                digits = []

                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())

                digits.reverse()
                k = int("".join(digits))

                stack.append(k * substr)

        return "".join(stack)


# class Solution:
#     def decodeString(self, s: str) -> str:
#         cur_num, cur_str = 0, []
#         num_stack, str_stack = [], []

#         for c in s:
#             if c.isdigit():
#                 cur_num = 10 * cur_num + int(c)
#             elif c == "[":
#                 str_stack.append(cur_str)
#                 num_stack.append(cur_num)
#                 cur_num, cur_str = 0, []
#             elif c == "]":
#                 last_num = num_stack.pop()
#                 last_str = str_stack.pop()
#                 cur_str = last_str + cur_str * last_num
#             else: # c.isalpha()
#                 cur_str.append(c)

#         return "".join(cur_str)


#  a2[b3[c]]d
#         ^
# cur_num = 0
# cur_str = ['c', 'b', 'b', 'b']
# num_stack = [['a'], ]
# str_stack = [2, ]

# last_num = 3
# last_str = ['b']



# class Solution:
#     def decodeString(self, s: str) -> str:
#         result, _ = self._decode_part(s, 0)
#         return result

#     def _decode_part(self, s: str, i: int):
#         """
#         return the decoded string and the index of next char that not decoded yet
#         """
#         result = []
#         num = 0

#         while i < len(s):
#             ch = s[i]

#             if ch.isdigit():
#                 num = num * 10 + int(ch)
#                 i += 1

#             elif ch == '[':
#                 inner, i = self._decode_part(s, i + 1)
#                 result.append(inner * num)
#                 num = 0
#                 i += 1

#             elif ch == ']':
#                 return ''.join(result), i

#             else:
#                 result.append(ch)
#                 i += 1

#         return ''.join(result), i
